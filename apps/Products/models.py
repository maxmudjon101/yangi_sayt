from django.db import models
from apps.base.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=200,null=False,blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description =models.CharField(max_length=200,null=False,blank=False)
    price = models.DecimalField(max_length=10,decimal_places=2)


    def __str__(self):
        return self.name