# accounts/serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MongoTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Force user ID to be a string
        token['user_id'] = str(user.id)
        return token

# serializers.py
from rest_framework import serializers
from .models import Ingredient

class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField()
    benefits = serializers.ListField(child=serializers.CharField(), required=False)
    description = serializers.CharField(required=False)
    warnings = serializers.ListField(child=serializers.CharField(), required=False)
    tags = serializers.ListField(child=serializers.CharField(), required=False)
    aromatherapy_uses = serializers.CharField(required=False)  