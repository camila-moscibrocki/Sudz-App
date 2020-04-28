from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['razao_social', 'cnpj', 'area', 'bio', 'photo']
