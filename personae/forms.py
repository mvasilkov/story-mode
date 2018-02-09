from django import forms

from .models import Persona
from .validators import persona_name_val


class PersonaForm(forms.Form):
    name = forms.CharField(min_length=6, max_length=64, validators=persona_name_val, strip=True)

    def clean_name(self):
        name = self.cleaned_data['name']
        if Persona.objects.filter(name=name).exists():
            raise forms.ValidationError('A persona with the same name already exists')
        return name
