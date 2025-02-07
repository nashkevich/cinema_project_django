from django.db import models
from cinema_back.utils.model_abstracts import Model

# Create your models here.
class Movie(Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    cast = models.JSONField(default=list)
    genres = models.JSONField(default=list)
    description = models.TextField()
    poster = models.CharField(max_length=300)
