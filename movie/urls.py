from django.urls import path

from .views import MovieList, ShowMovieDetail


app_name = "movie"

urlpatterns = [
    path('watch/<str:profile_id>/', MovieList.as_view(), name="movie_list"),
    path('movie/detail/<str:movie_id>/', ShowMovieDetail.as_view(), name="movie_detail"),
]