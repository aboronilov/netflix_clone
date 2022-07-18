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
        if profile_id:
            profile = Profile.objects.get(uuid=profile_id)
            if profile in request.user.profiles.all():
                movies = Movie.objects.filter(age_limit=profile.age_limit)
                context = {
                    'movies': movies
                }
                return render(request, 'movieList.html', context=context)            
            return redirect(to="core:profile_list")
        return render(request, 'movieList.html')
            

