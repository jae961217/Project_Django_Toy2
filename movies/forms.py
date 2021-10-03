from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):

    class Meta: # form에 대한 정보
        model = Movie
        fields = '__all__'