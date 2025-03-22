# accounts/authentication.py
from django.contrib.auth.backends import BaseBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User

class MongoEngineBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Treat 'username' as the email.
        user = User.objects(email=username).first()
        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

class MongoJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            # Get the user ID from the token using the claim defined in SIMPLE_JWT
            user_id = validated_token.get(self.get_user_id_claim())
            # Lookup the user with MongoEngine. The user_id is a string.
            return User.objects.get(id=user_id)
        except Exception:
            return None
