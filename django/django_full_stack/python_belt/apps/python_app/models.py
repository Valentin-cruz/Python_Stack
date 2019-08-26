from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 150)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Item(models.Model):
    title=models.CharField(max_length=64)
    user=models.ForeignKey(User, related_name='items', on_delete = models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Wish(models.Model):
    wish=models.ForeignKey(Item, related_name='wishers', on_delete = models.CASCADE)
    wisher=models.ForeignKey(User, related_name='wishes', on_delete = models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)