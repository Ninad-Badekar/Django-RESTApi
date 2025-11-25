from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Product, Brand, Category
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer 
from drf_spectacular.utils import extend_schema

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)