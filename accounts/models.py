from django.db import models

# Create your models here.

from mongoengine import Document, StringField
from passlib.hash import bcrypt

class User(Document):
    email = StringField(required=True, unique=True)
    password_hash = StringField(required=True)

    def set_password(self, raw_password):
        """Hash and set the password."""
        self.password_hash = bcrypt.hash(raw_password)

    def check_password(self, raw_password):
        """Verify a raw password against the stored hash."""
        return bcrypt.verify(raw_password, self.password_hash)
