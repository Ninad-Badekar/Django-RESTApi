from rest_framework import serializers
from .models import Product,Brand,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = "__all__"

