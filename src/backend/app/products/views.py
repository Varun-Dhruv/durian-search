import concurrent.futures

from products.parser import scrape_website
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
        products = []
        for website in data["websites"]:
            if website not in ["flipkart", "amazon", "snapdeal"]:
                return Response({"error": "Invalid website"}, status=400)
        total = int(data["total_products"]) if data["total_products"] else 3
        with concurrent.futures.ThreadPoolExecutor() as executor:
            tasks = zip(
                data["websites"], [data["search_term"]] * len(data["websites"]), [total] * len(data["websites"])
            )
            products = [item for sublist in executor.map(scrape_website, *zip(*tasks)) for item in sublist]

        return Response({"products": products}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


# Create your views here.
