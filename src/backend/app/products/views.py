import concurrent.futures

from django.db.models import OuterRef, Subquery
from products.models import Product
from products.parser import COMPANIES, scrape_website
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_products(request):
    try:
        data = {
            "search_term": request.query_params.get("searchTerm"),
            "total_products": request.query_params.get("totalProducts"),
            "websites": request.query_params.getlist("websites"),
            "price_min": request.query_params.get("minPrice"),
            "price_max": request.query_params.get("maxPrice"),
            "rating_min": request.query_params.get("minRating"),
            "rating_max": request.query_params.get("maxRating"),
            "reviews_min": request.query_params.get("minReviews"),
            "reviews_max": request.query_params.get("maxReviews"),
        }

        data["websites"] = data["websites"][0].split(",") if data["websites"] else []

        total = int(data["total_products"]) if data["total_products"] else 3
        # check if the websites are valid or not
        for website in data["websites"]:
            if website not in ["flipkart", "amazon", "snapdeal", "blinkit", "jiomart"]:
                return Response({"error": "Invalid website"}, status=400)
        products = Product.objects.filter(search_term=data["search_term"])
        # check if the search already exists in database
        if products.exists():
            subquery = Product.objects.filter(company=OuterRef("company")).order_by("-created_at")[:total].values("id")
            result = Product.objects.filter(company__in=data["websites"], id__in=Subquery(subquery))
            serializer = ProductSerializer(result, many=True)
            return Response({"products": serializer.data}, status=200)
        # else scrape from the web
        else:
            products = []

            with concurrent.futures.ThreadPoolExecutor() as executor:
                tasks = zip(
                    data["websites"], [data["search_term"]] * len(data["websites"]), [total] * len(data["websites"])
                )
                products = [item for sublist in executor.map(scrape_website, *zip(*tasks)) for item in sublist]

            bulk_products_objects = []
            for product in products:
                if product["rating"] == "N/A":
                    product["rating"] = None
                if product["total_review_count"] == "N/A":
                    product["total_review_count"] = None

                bulk_products_objects.append(
                    Product(
                        search_term=data["search_term"],
                        title=product["title"],
                        url=product["url"],
                        total_review_count=product["total_review_count"],
                        rating=product["rating"],
                        price=product["price"],
                        website=product["website"],
                        company=COMPANIES[product["website"]],
                    )
                )
            Product.objects.bulk_create(bulk_products_objects)
            return Response({"products": products}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
