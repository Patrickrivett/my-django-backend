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
    

class Product(models.Model):
     name        = models.CharField(max_length=200)
     price       = models.DecimalField(max_digits=6, decimal_places=2)
     image       = models.ImageField(upload_to='products/')  # Cloudinary‑backed
     category    = models.CharField(max_length=50)
     tags        = models.JSONField(default=list)
     description = models.TextField(blank=True)  

     def __str__(self):
         return self.name