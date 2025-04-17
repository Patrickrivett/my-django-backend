from django.db import models

# Create your models here.
class Product(models.Model):
     name        = models.CharField(max_length=200)
     price       = models.DecimalField(max_digits=6, decimal_places=2)
     image       = models.ImageField(upload_to='products/')  # Cloudinary‑backed
     category    = models.CharField(max_length=50)
     tags        = models.JSONField(default=list)
     description = models.TextField(blank=True)  

     def __str__(self):
         return self.name
