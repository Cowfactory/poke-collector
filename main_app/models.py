from django.conf import settings
from django.db import models

ELEMENT = (
    ('Normal', 'Normal'),
    ('Fighting', 'Fighting'),
    ('Flying', 'Flying'),
    ('Poison', 'Poison'),
    ('Ground', 'Ground'),
    ('Rock', 'Rock'),
    ('Bug', 'Bug'),
    ('Ghost', 'Ghost'),
    ('Fire', 'Fire'),
    ('Water', 'Water'),
    ('Grass', 'Grass'),
    ('Electric', 'Electric'),
    ('Psychic', 'Psychic'),
    ('Ice', 'Ice'),
    ('Dragon', 'Dragon'),
)
GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

# Create your models here.
class CaughtPokemon(models.Model):
    trainer_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        #user = models.ForeignKey(User, on_delete=models.CASCADE)?
        on_delete = models.CASCADE
    )
    pokedex_id = models.ForeignKey(
        'PokedexPokemon',
        on_delete = models.CASCADE
    )
    gender = models.CharField(
        max_length = 6,
        choices = GENDER,
        default = GENDER[0]
    )
    level = models.IntegerField()
    capture_date = models.DateField()
    

class PokedexPokemon(models.Model):      
    pokedex_id = models.CharField(max_length=4)
    element_type = models.CharField(
        max_length = 10,
        choices = ELEMENT,
        default = ELEMENT[0]
    )
    evolution_lvl = models.IntegerField()
    moveset = models.CharField(max_length=10) #Fix this later to be a real move set

