from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # called once at Django startup
        import mongoengine
        from django.conf import settings

        # establish your Atlas connection (won’t block on import)
        mongoengine.connect(
            db=settings.MONGO_DB_NAME,
            host=settings.MONGO_HOST,
            connect=False,                  # defer TCP handshake
            serverSelectionTimeoutMS=3000,  # 3s max for server-selection
        )
