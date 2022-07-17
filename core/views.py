from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import ProflieCreateForm
from .models import Profile

class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # return render(request, 'profileList.html')
            return redirect('core:profile_list')
        return render(request, 'index.html')

@method_decorator(login_required, name="dispatch")   
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()
        context={'profiles':profiles}
        return render(request, 'profileList.html', context=context)

@method_decorator(login_required, name="dispatch")      
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        form = ProflieCreateForm()
        context = {
            'form': form
        }
        return render(request, 'profileCreate.html', context=context)
    
    def post(self, request, *args, **kwargs):
        form = ProflieCreateForm(request.POST or None)
        context = {
            'form': form
        }
        if form.is_valid():            
            instance = form.cleaned_data
            profile = Profile.objects.create(**instance)
            if profile:
                request.user.profiles.add(profile)
                return redirect('core:profile_list')
        return render(request, 'profileCreate.html', context=context)