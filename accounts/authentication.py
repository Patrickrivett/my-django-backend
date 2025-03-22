from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User

class MongoJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        """
        Override the default get_user method so that we can use MongoEngine
        and treat the user ID as a string.
        """
        try:
            # Get the user ID from the token using the claim defined in SIMPLE_JWT
            user_id = validated_token.get(self.get_user_id_claim())
            # Lookup the user with MongoEngine
            return User.objects.get(id=user_id)
        except Exception as e:
            return None
