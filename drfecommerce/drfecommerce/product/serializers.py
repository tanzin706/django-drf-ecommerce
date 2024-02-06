from rest_framework import serializers

from .models import Brand, Category, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="name")

    class Meta:
        model = Category
        fields = ["category_name"]
        # fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ("id",)
        # fields = ["name"]
        # fields = "__all__"


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        exclude = ("id", "is_active", "product")


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(
        source="brand.name"
    )  ###This is foreign key in Product###
    category_name = serializers.CharField(
        source="category.name"
    )  ###This is foreign key in Product###
    ###category=CategorySerializer()
    product_line = ProductLineSerializer(
        many=True
    )  ###this is related_name in ProductLine models product(field) foreign key###

    class Meta:
        model = Product
        fields = (
            "name",
            "slug",
            "description",
            "brand_name",
            "category_name",
            "product_line",
        )
