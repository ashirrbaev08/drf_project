from rest_framework import serializers
from .models import Category,Product,Review
from rest_framework.exceptions import ValidationError


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

    def get_negative_reviews(self,obj):
        return obj.negative_reviews()


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

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def validate_category_id(self,category_id):
        try:
            Category.objects.get(id=category_id)
        except:
            raise ValidationError('this category does not exist!')

        return category_id



class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    product_id = serializers.IntegerField()
    stars = serializers.IntegerField()

    def validate_product_id(self,product_id):
        try:
            Product.objects.get(id=product_id)
        except:
            raise ValidationError('this product does not exist!')
        return product_id