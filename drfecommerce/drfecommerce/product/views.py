from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A Simple Viewset for viewing all Categoreis
    """

    queryset = Category.objects.all()  # database to django(queryset)

    @extend_schema(
        responses=CategorySerializer
    )  # tell drf spectacular which serializer is used for documentation
    def list(self, request):
        serializer = CategorySerializer(
            self.queryset, many=True
        )  # django to serializer
        return Response(serializer.data)  # serializer to response


class BrandViewSet(viewsets.ViewSet):
    """
    A Simple Viewset for viewing all Brands
    """

    queryset = Brand.objects.all()  # database to django(queryset)

    @extend_schema(
        responses=BrandSerializer
    )  # tell drf spectacular which serializer is used for documentation
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)  # django to serializer
        return Response(serializer.data)  # serializer to response


class ProductViewSet(viewsets.ViewSet):
    """
    A Simple Viewset for viewing all Products
    """

    queryset = Product.objects.all()  # database to django(queryset)

    @extend_schema(
        responses=ProductSerializer
    )  # tell drf spectacular which serializer is used for documentation
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)  # django to serializer
        return Response(serializer.data)  # serializer to response
