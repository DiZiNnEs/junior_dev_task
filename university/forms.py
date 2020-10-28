from django.forms import ModelForm
from .models import University


class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = '__all__'
