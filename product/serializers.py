from rest_framework import serializers
from .models import Category,Product,Review


class CategoryListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id','name','products']

    def get_products(self,obj):
        return obj.quantity_of_product()


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id','title','price','reviews','rating']
        depth = 1

    def get_reviews(self,obj):
        return obj.review_names()
    
    def get_rating(self,rating):
        return rating.product_rating()


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class RewiewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','text']
        
class RewiewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'