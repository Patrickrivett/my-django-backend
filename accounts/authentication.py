from django.contrib.auth.backends import BaseBackend
from .models import User

class MongoEngineBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Use email as username
        user = User.objects(email=username).first()
        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
