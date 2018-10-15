from django.forms import ModelForm, Form, DateField, CharField, PasswordInput, CheckboxSelectMultiple
from .models import CaughtPokemon

class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())

class PokemonForm(ModelForm):
    class Meta:
        model = CaughtPokemon
        fields = ['pokedex_id', 'gender', 'level', 'description', 'capture_date']
        widgets = {
            'gender': CheckboxSelectMultiple,
            'capture_date': DateField,
        }