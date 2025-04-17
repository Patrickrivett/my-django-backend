# products/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product

@api_view(['GET'])
def product_list(request):
    """
    GET /api/products/ → Return all products from MongoDB Atlas
    """
    docs = Product.objects  # mongoengine QuerySet
    # Convert each document to a plain dict
    data = [doc.to_dict() for doc in docs]
    return Response(data)
