# accounts/authentication.py
from django.contrib.auth.backends import BaseBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User

class MongoEngineBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = User.objects(email=username).first()
        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from .models import User
import logging

logger = logging.getLogger(__name__)

class MongoJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            
            user_id_claim = api_settings.USER_ID_CLAIM
            user_id = validated_token.get(user_id_claim)

            logger.info(f"Token user_id: {user_id}")

            user = User.objects.get(id=user_id)
            logger.info(f"Found user: {user.email}")
            return user
        except Exception as e:
            logger.error(f"Error in get_user: {e}")
            return None
