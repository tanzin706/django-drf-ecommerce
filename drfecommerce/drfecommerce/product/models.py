from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# class ActiveManager(models.Manager):
#     # def get_queryset(self):
#     #     return super().get_queryset().filter(is_active=True)
#     def isactive(self):
#         return self.get_queryset().filter(is_active=True)


#     def all(self):
#         return self.get_queryset().all()
class ActiveQueryset(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)

    def all(self):
        return self


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True
    )  # if you want to delete category, then u first have to delete all the entries of it first...example: want to del clothes(u 1st need to del shirts and pants)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE
    )  # if brand is deleted all products of that brand will be deleted
    category = TreeForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,  ### Category is in quotation Because of Category model is MPTT###
    )
    is_active = models.BooleanField(default=False)

    objects = ActiveQueryset.as_manager()
    # objects = models.Manager()  #### this manager gives every data###
    # isactive = ActiveManager()  ### this manager only give active data###

    def __str__(self):
        return self.name


class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=5)
    sku = models.CharField(max_length=100)
    stock_qty = models.IntegerField()
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="product_line"
    )  ### Product is in quotation Because of Product model has Category model in it which is MPTT###
    is_active = models.BooleanField(default=False)
