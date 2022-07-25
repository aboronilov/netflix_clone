from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from core.models import Profile
from .models import Movie

from random import choice

@method_decorator(login_required, name="dispatch")
class MovieList(View):
    def get(self, request, *args, **kwargs):
        profile_id = kwargs.get("profile_id")
        try:
            profile = Profile.objects.get(uuid=profile_id)
        except Profile.DoesNotExist:
            return redirect(to="core:profile_list")
        else:    
            if profile in request.user.profiles.all():
                # movies = Movie.objects.filter(age_limit=profile.age_limit)
                # try:
                #     showcase = movies.first()
                # except showcase.DoesNotExist:
                #     pass
                # context = {
                #     'movies': movies,
                #     'show_case': showcase
                # }
                movies_pks = Movie.objects.values_list('pk', flat=True)
                if len(movies_pks) > 0:
                    random_pk = choice(movies_pks)
                    random_movie = Movie.objects.get(pk=random_pk)
                    other_movies = Movie.objects.exclude(pk=random_pk)
                    context = {
                        'random_movie': random_movie,
                        'other_movies': other_movies,
                    }
                    return render(request, 'movieList.html', context=context)
                else:
                    return redirect(to='core:home')
        return render(request, 'movieList.html')
            

@method_decorator(login_required, name="dispatch")
class ShowMovieDetail(View):
    def get(self, request, *args, **kwargs):
        movie_id = kwargs.get('movie_id')
        try:
            movie = Movie.objects.get(uuid=movie_id)
        except Movie.DoesNotExist:
            return redirect(to="core:profile_list")
        else:
            other_movies = Movie.objects.exclude(uuid=movie_id)
            context = {
                'movie': movie,
                'other_movies': other_movies
            }
            return render(request, 'movieDetail.html', context=context)
        

@method_decorator(login_required, name="dispatch")
class ShowMovie(View):
    def get(self, request, *args, **kwargs):
        movie_id = kwargs.get('movie_id')
        try:
            movie = Movie.objects.get(uuid=movie_id)
        except Movie.DoesNotExist:
            return redirect(to="core:profile_list")
        else:
            videos = movie.videos.values()
            context = {
                'movie': list(videos)
            }
            return render(request, 'showMovie.html', context=context)

