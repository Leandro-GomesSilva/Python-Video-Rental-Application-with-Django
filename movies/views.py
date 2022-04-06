from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie  # importando os models

# Create your views here.


def index(request):
    # SELECT * FROM movies_movie
    movies = Movie.objects.all()

    render(request, 'index.html', {'movies': movies})

    # SELECT * FROM movies_movie WHERE
    # Movie.objects.filter(release_year=1984)

    # return HttpResponse("Hello World")

    return render(request, 'index.html', {'movies': movies})


def detail(request, movie_id):
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()

    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
