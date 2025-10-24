from rest_framework import serializers
from .models import (
    Product, Category, ProductImage,
    SizeVariant, ColorVariant, Tag, ProductTag
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text']


class SizeVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        fields = ['id', 'size', 'stock']


class ColorVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariant
        fields = ['id', 'color_name', 'hex_code', 'image']



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class ProductTagSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True)

    class Meta:
        model = ProductTag
        fields = ['id', 'tag']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    sizes = SizeVariantSerializer(many=True, read_only=True)
    colors = ColorVariantSerializer(many=True, read_only=True)
    tags = ProductTagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price', 'stock',
            'brand', 'is_active', 'category', 'created_at', 'updated_at',
            'images', 'sizes', 'colors', 'tags'
        ]