# backend/accounts/apps.py
from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # Called once, at Django startup, before any auth or view code runs
        import mongoengine
        from django.conf import settings

        mongoengine.connect(
            db=settings.MONGO_DB_NAME,
            host=settings.MONGO_HOST,
            connect=False,
            serverSelectionTimeoutMS=3000,
        )
