from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from core.models import Profile
from .models import Movie

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
                movies = Movie.objects.filter(age_limit=profile.age_limit)
                try:
                    showcase = movies.first()
                except showcase.DoesNotExist:
                    pass
                context = {
                    'movies': movies,
                    'show_case': showcase
                }
                return render(request, 'movieList.html', context=context)
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
            context = {
                'movie': movie
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

