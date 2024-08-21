from django.db import models
from apps.base.models import BaseModel
from apps.base.file_path_renaimer import PathRename
from django.core.validators import FileExtensionValidator

product_thumbnail_path = PathRename("products")
product_gallery_path = PathRename("products_gallery")


class Category(BaseModel):
    name = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=200,null=False,blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description =models.CharField(max_length=200,null=False,blank=False)
    thumbnail = models.ImageField(null=False,blank=False,upload_to=product_thumbnail_path,validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])])
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural  = "Mahsulotlar"


    def __str__(self):
        return self.name


class PhotoProductGallery(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo =models.ImageField(null=False,blank=False,upload_to=product_gallery_path,validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])])





























































