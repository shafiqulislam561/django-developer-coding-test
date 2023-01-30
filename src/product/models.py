from django.db import models
from config.g_model import TimeStampMixin


# Create your models here.
class Variant(models.Model):
    title = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created_at  = models.TimeField()
    updated_at = models.TimeField()

    def __str__(self):
        return self.title or ''


class Product(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    sku = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at  = models.TimeField()
    updated_at = models.TimeField()

    def __str__(self):
        return self.title or ''


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_path = models.URLField()
    thumbnail = models.SmallIntegerField()
    created_at  = models.TimeField()
    updated_at = models.TimeField()

    def __str__(self):
        return self.product.title or ''


class ProductVariant(models.Model):
    variant_title = models.CharField(max_length=255)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at  = models.TimeField()
    updated_at = models.TimeField()

    def __str__(self):
        return self.variant_title or ''


class ProductVariantPrice(models.Model):
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                              related_name='product_variant_three')
    price = models.FloatField()
    stock = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at  = models.TimeField()
    updated_at = models.TimeField()

    def __str__(self):
        return self.product.title or ''