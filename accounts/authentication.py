from django.contrib.auth.backends import BaseBackend
from .models import User

class MongoEngineBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 'username' is typically the user ID or email passed by Simple JWT
        user = User.objects(email=username).first()
        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        # user_id is your ObjectId as a string
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
