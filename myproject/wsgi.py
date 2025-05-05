"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

# 1️⃣ Ensure Django knows which settings to load
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# 2️⃣ Now you can safely import settings and connect to MongoDB
import mongoengine
from django.conf import settings

mongoengine.connect(
    db=settings.MONGO_DB_NAME,
    host=settings.MONGO_HOST,
    alias='default',
    connect=False,
    serverSelectionTimeoutMS=3000,
)

# 3️⃣ Finally, get the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
