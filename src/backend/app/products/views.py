from products.parser import scrape_amazon, scrape_flipkart, scrape_snapdeal
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_products(request):
    try:
        data = {
            "search_term": request.query_params.get("searchTerm"),
            "websites": request.query_params.getlist("websites"),
            "price_min": request.query_params.get("minPrice"),
            "price_max": request.query_params.get("maxPrice"),
            "total_products": request.query_params.get("totalProducts"),
        }
        data["websites"] = data["websites"][0].split(",") if data["websites"] else []

        for website in data["websites"]:
            if website == "flipkart":
                flipkart_products = scrape_flipkart(data["search_term"])
            elif website == "amazon":
                amazon_products = scrape_amazon(data["search_term"])
            elif website == "snapdeal":
                snapdeal_products = scrape_snapdeal(data["search_term"])
            else:
                return Response({"error": "Invalid website"}, status=400)
        total = int(data["total_products"])
        products = flipkart_products[:total] + amazon_products[:total] + snapdeal_products[:total]
        return Response({"products": products}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


# Create your views here.
