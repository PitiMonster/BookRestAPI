from django.db import models
from django_mysql.models import ListCharField

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = ListCharField(base_field=models.CharField(max_length=50), size=10, max_length=(50 * 11))
    published_date = models.DateField()
    categories = ListCharField(base_field=models.CharField(max_length=50), size=10, max_length=(50 * 11))
    average_rating = models.IntegerField(default=None)
    ratings_count = models.IntegerField(default=None)
    thumbnail = models.URLField()

    def __str__(self):
        return f'{self.title} published by {self.authors}'

    class Meta:
        ordering = ['published_date']
