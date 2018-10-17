from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PokedexPokemon)
admin.site.register(CaughtPokemon)
admin.site.register(Profile)
admin.site.register(PokeField)
admin.site.register(PokemonList)

