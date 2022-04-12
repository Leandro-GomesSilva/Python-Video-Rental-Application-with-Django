from django.urls import path
from . import views  # Note for me: Explica no vídeo 4, 4:16, porque isso deve ser assim

app_name = 'movies'  # Note for me: Vem do vídeo 18, 'Referencing Urls'

# movies/
urlpatterns = [
    # The path '' represents the root
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
