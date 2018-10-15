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
    nickname = models.CharField(max_length=20)
    level = models.IntegerField()
    description = models.CharField(max_length=200)
    capture_date = models.DateField()
    

class PokedexPokemon(models.Model):      
    pokedex_id = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    type1 = models.CharField(max_length=10)
    type2 = models.CharField(max_length=10, null=True)
    # evolution_lvl = models.IntegerField()
    # moveset = models.CharField(max_length=10) #Fix this later to be a real move set
    art_url = models.CharField(max_length=200)
    early_art_url = models.CharField(max_length=200)
    early_jp_art_url = models.CharField(max_length=200)
    icon_url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.pokedex_id}"