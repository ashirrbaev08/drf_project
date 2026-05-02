from django.db import models
from django.db.models import Avg
from django.db.models import Count

class Category(models.Model):

    name = models.CharField(max_length=255)

    def quantity_of_product(self):
        return self.products.count()

    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField()
    description = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
   
    def __str__(self):
        return self.title

    def review_names(self):
        return [i.text for i in self.reviews.all()]

    def product_rating(self):
        reviews = self.reviews.all()
        if not reviews:
            return 0

        total = sum(i.stars for i in reviews)
        return total / reviews.count()
        
    
class Review(models.Model):
    text = models.CharField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=((i,'*' * i) for i in range(1,6)),
                                default=5)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,
                                related_name='reviews')

    def __str__(self):

        return self.text


