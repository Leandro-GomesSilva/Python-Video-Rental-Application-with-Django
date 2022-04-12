from django.db import models
from django.utils import timezone

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField
    place_of_birth = models.CharField(max_length=255)
    wikipedia_article = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    length = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    synopsis = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    main_cast = models.ManyToManyField(Actor)
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    # A common recommendation is to implement it in a way so that it is 'aware' of timezones
    date_created = models.DateTimeField(default=timezone.now)
