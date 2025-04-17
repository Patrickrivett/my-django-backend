# accounts/serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MongoTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = str(user.id)
        return token

# serializers for ingredients and then problems (ingredient and problem search models)
from rest_framework import serializers
from .models import Ingredient

class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField()
    benefits = serializers.ListField(child=serializers.CharField(), required=False)
    description = serializers.CharField(required=False)
    warnings = serializers.ListField(child=serializers.CharField(), required=False)
    tags = serializers.ListField(child=serializers.CharField(), required=False)
    aromatherapy_uses = serializers.CharField(required=False)  


class ProblemSerializer(serializers.Serializer):
    name = serializers.CharField()
    ingredients = serializers.ListField(child=serializers.CharField(), required=False)
    description = serializers.CharField(required=False)
    tags = serializers.ListField(child=serializers.CharField(), required=False)

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    imageUrl    = serializers.ImageField(source='image', read_only=True)
    description = serializers.CharField(read_only=True)

    class Meta:
        model  = Product
        fields = ['id', 'name', 'description', 'price',
                  'imageUrl', 'category', 'tags']