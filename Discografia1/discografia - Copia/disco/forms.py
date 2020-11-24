from django import forms
from .models import Musicas
from django.forms import Select, TextInput, NumberInput


class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musicas
        fields = [
            'titulo',
            'segundos',
            'album',
        ]
        widgets = {
            'titulo': TextInput(),      #attrs = {'class': 'classe do elemento'}
            'segundos': NumberInput(),  #attrs = {'class': 'classe do elemento'}
            'album': Select(),          #attrs = {'class': 'classe do elemento'}
        }