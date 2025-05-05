from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product

@api_view(['GET'])
def product_list(request):
    """
    GET /api/products/ → Return all products from MongoDB Atlas
    """
    docs = Product.objects   # uses the single default connection from wsgi.py
    data = [doc.to_mongo().to_dict() for doc in docs]
    return Response(data)
