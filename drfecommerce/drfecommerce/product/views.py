from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import connection
from pygments import highlight  ## to highlight sql ##
from pygments.formatters import TerminalFormatter  ## for terminal format view   ##
from pygments.lexers import SqlLexer

# for sqlite database formatter view on console, different bd different Lexer
from sqlparse import format  ##only to view sql##

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

    queryset = Product.objects.isactive()  # database to django(queryset)
    lookup_field = "slug"

    @extend_schema(
        responses=ProductSerializer
    )  # tell drf spectacular which serializer is used for documentation
    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(
            self.queryset.filter(slug=slug).select_related(
                "category", "brand"
            ),  ### category and brand has one to many relation with product, data from these 2 tables are being fetched without any queries###cat -> pro, bran -> pro###
            many=True,
            # self.queryset.filter(slug=slug), many=True
        )  # django to serializer
        data = Response(serializer.data)

        q = list(connection.queries)
        print(len(q))
        for qs in q:
            sqlformatted = format(str(qs["sql"]), reindent=True)
            print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
        # x = self.queryset.filter(slug=slug)
        # sqlformatted = format(str(x.query), reindent=True)
        # print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))

        return data

    def list(self, request):
        serializer = ProductSerializer(
            self.queryset.select_related("category", "brand"),
            many=True,
        )  # django to serializer
        data = Response(serializer.data)  # serializer to response

        q = list(connection.queries)
        print(len(q))
        for qs in q:
            sqlformatted = format(str(qs["sql"]), reindent=True)
            print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
        return data

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<category>\w+)/all",  ##P<category> is identifying <category>,? means 0 or 1 characters and \w+ means anything besides space before\w+
    )
    def list_product_by_category(self, request, category=None):
        """
        An Endpoint to return product by category
        """
        serializer = ProductSerializer(
            self.queryset.filter(category__name=category), many=True
        )  # Here there is a product query,in which category is a foreign key(id).by using "__name" we access that categorys name.with provided category(param) name match it with the filtered category__name products.
        return Response(serializer.data)  # serializer to response
