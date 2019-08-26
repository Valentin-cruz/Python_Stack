from django.db import models

class Show(models.Model):
    title = models.CharField(max_length = 60)
    network = models.CharField(max_length = 60)
    release = models.DateTimeField()
    description = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)