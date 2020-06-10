from django.forms import ModelForm
from .models import Opony

class OponaForm(ModelForm):
    class Meta:
        model = Opony
        fields = ['producent','modelnazwa','szerokosc','profil','srednica','opis','rok_produkcji', 'zdjecie']

