# accounts/serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MongoTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Force user ID to be a string
        token['user_id'] = str(user.id)
        return token
