from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    descripation=models.CharField(max_length=200)
    image=models.ImageField(upload_to='static/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()
