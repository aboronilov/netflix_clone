from django.urls import path

from .views import MovieList, ShowMovie, ShowMovieDetail


app_name = "movie"

urlpatterns = [
    path('watch/<str:profile_id>/', MovieList.as_view(), name="movie_list"),
    path('movie/detail/<str:movie_id>/', ShowMovieDetail.as_view(), name="movie_detail"),
    path('movie/play/<str:movie_id>/', ShowMovie.as_view(), name='play'),
]