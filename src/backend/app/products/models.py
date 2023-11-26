from django.db import models
from django.utils import timezone


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    search_term = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.TextField()
    total_review_count = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    price = models.FloatField(default=0)
    website = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
