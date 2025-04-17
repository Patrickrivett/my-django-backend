from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    imageUrl    = serializers.ImageField(source='image', read_only=True)
    description = serializers.CharField(read_only=True)

    class Meta:
        model  = Product
        fields = ['id', 'name', 'description', 'price', 'imageUrl', 'category', 'tags']
