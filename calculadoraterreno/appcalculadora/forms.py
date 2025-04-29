from django import forms
from .models import PlanoUrbano

class FormularioTerreno(forms.ModelForm):
    class Meta:
        model = PlanoUrbano
        fields = '__all__'