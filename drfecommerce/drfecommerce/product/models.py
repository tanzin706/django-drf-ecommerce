from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True
    )  # if you want to delete category, then u first have to delete all the entries of it first...example: want to del clothes(u 1st need to del shirts and pants)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE
    )  # if brand is deleted all products of that brand will be deleted
    category = TreeForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name
