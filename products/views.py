# products/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

# bring in your Document
from .models import Product

# bring in mongoengine and settings
import mongoengine
from django.conf import settings
from pymongo import errors

@api_view(['GET'])
def product_list(request):
    """
    GET /api/products/ → Return all products from MongoDB Atlas
    """
    # 1) connect on each request (but no import‐time hang)
    try:
        mongoengine.connect(
            db=settings.MONGO_DB_NAME,
            host=settings.MONGO_HOST,
            connect=False,                  # defer SRV/DNS until first query
            serverSelectionTimeoutMS=3000,  # 3 s max for server handshake
        )
    except errors.ServerSelectionTimeoutError:
        return Response(
            {"error": "Cannot connect to database."},
            status=503
        )

    # 2) now do your normal query:
    docs = Product.objects  # mongoengine QuerySet
    data = [doc.to_mongo().to_dict() for doc in docs]
    return Response(data)
