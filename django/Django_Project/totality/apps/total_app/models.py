from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 150)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    reviewer = models.ForeignKey(User, related_name= 'written_reviews', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name = 'reviews', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Order(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    address = models.CharField(max_length=40, blank=False)
    city = models.CharField(max_length=40, blank=False)
    zipcode = models.CharField(max_length=20, blank=False)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

class Wish(models.Model):
    wish=models.ForeignKey(Product, related_name='wishers', on_delete = models.CASCADE)
    wisher=models.ForeignKey(User, related_name='wishes', on_delete = models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    users_c = models.ForeignKey(User, related_name="c_users", on_delete=models.CASCADE)
    review_c = models.ForeignKey(Review, related_name="c_review",on_delete=models.CASCADE)
    comment = models.CharField(max_length = 150)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)