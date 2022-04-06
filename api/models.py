from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# Create your models here.


class MovieResource(ModelResource):
    class Meta:
        # Set this to the query to get the list of all movies
        queryset = Movie.objects.all()
        resource_name = 'movies'
        excludes = ['date_created']
