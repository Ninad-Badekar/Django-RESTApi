from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Product, Brand, Category
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer 

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer   # ✅ REQUIRED

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
