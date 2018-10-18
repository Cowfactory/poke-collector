from django.forms import ModelForm, Form, DateField, CharField, PasswordInput, CheckboxSelectMultiple
from .models import CaughtPokemon, Profile

class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location')

class PokemonForm(ModelForm):
    class Meta:
        model = CaughtPokemon
        fields = '__all__'
        # exclude = ['preferred_img']

        