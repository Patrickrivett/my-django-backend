from django.shortcuts import render

# Create your views here.
# ------------------------- view for product view set -------------------------

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset         = Product.objects.all()
    serializer_class = ProductSerializer
