from django.contrib import admin

# Register your models here.
from .models import Brand, Category, Product, ProductLine


class ProductLineInline(admin.TabularInline):
    model = ProductLine


@admin.register(
    Product
)  ###Registers product and the class below this is to connect the productline table with product table###
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductLine)
