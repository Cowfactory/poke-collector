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
        # fields = ['identifier', 'gender', 'level', 'description', 'capture_date']
        fields = '__all__'
        widgets = {
            # 'gender': CheckboxSelectMultiple,
            # 'capture_date': DateField,
        }

        