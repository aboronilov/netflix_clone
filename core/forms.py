from .models import Profile
from django.forms import ModelForm


class ProflieCreateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'age_limit']