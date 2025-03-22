from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MongoTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Convert user.id to string so it doesn't try to cast to int
        token['user_id'] = str(user.id)
        return token
