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

import logging

logger = logging.getLogger(__name__)

class MongoJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token.get(self.get_user_id_claim())  # e.g. 'user_id'
            logger.info(f"Token user_id: {user_id}")
            # Lookup the user by string ID
            user = User.objects.get(id=user_id)
            logger.info(f"Found user: {user.email}")
            return user
        except Exception as e:
            logger.error(f"Error in get_user: {e}")
            return None