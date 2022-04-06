from django.urls import path
from . import views     # Ele explica no vídeo 4, 4:16, porque isso deve ser desta forma #

# Isso vem do vídeo 18, Referencing Urls
app_name = 'movies'

# movies/
urlpatterns = [
    # Um path "" representa o root #
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
