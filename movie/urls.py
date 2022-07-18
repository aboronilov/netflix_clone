from django.urls import path

from .views import MovieList


app_name = "movie"

urlpatterns = [
    path('watch/<str:profile_id>/', MovieList.as_view(), name="movie_list")
]