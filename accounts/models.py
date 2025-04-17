from django.db import models
from mongoengine import Document, StringField, ListField

from mongoengine import Document, StringField
from passlib.hash import bcrypt

class User(Document):
    email = StringField(required=True, unique=True)
    password_hash = StringField(required=True)

    name = StringField()  
    age_group = StringField()  
    hair_types = ListField(StringField()) 
    skin_types = ListField(StringField()) 
    allergies = ListField(StringField())   

    def set_password(self, raw_password):
        """Hash and set the password."""
        self.password_hash = bcrypt.hash(raw_password)

    def check_password(self, raw_password):
        """Verify a raw password against the stored hash."""
        return bcrypt.verify(raw_password, self.password_hash)
    @property
    def is_active(self):
        return True
    @property
    def is_authenticated(self):
        return True


class Ingredient(Document):
    meta = {'collection': 'ingredients'}
    name = StringField(required=True, unique=True)
    benefits = ListField(StringField())
    description = StringField()
    warnings = ListField(StringField())
    tags = ListField(StringField())
    aromatherapy_uses = StringField()


class Problem(Document):
    meta = {'collection': 'problems'}
    name = StringField(required=True, unique=True)
    ingredients = ListField(StringField())
    description = StringField()
    tags = ListField(StringField())
    