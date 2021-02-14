from django import forms
from .models import *

class BandForm(forms.ModelForm):
    dof = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Band
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Album
        fields = '__all__'
