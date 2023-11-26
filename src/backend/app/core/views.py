from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_health(request):
    try:
        return Response({"message": "Alive and Kickin!"}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
