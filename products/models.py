# products/models.py
from mongoengine import Document, IntField, StringField, FloatField, ListField

class Product(Document):
    meta      = {'collection': 'products'}
    id        = IntField(primary_key=True)      # matches your existing `id` field
    name      = StringField(required=True)
    description = StringField()
    price     = FloatField(required=True)
    imageUrl  = StringField(required=True)
    category  = StringField()
    tags      = ListField(StringField())

    def to_dict(self):
        return {
            "id":          self.id,
            "name":        self.name,
            "description": self.description or "",
            "price":       self.price,
            "imageUrl":    self.imageUrl,
            "category":    self.category,
            "tags":        self.tags,
        }