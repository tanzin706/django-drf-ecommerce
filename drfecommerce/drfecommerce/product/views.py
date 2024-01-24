from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A Simple Viewset for viewing all Categoreis
    """

    queryset = Category.objects.all()  # database to django(queryset)

    def list(self, request):
        serializer = CategorySerializer(
            self.queryset, many=True
        )  # django to serializer
        return Response(serializer.data)  # serializer to response
