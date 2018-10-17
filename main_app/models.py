from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from random import seed
from random import randint

# Seed random number generator
seed(1)

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
class Profile(models.Model): #extended user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(
        max_length=500, 
        blank=True,
        null = True,
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        null = True,
    )
    # favorites = models.CharField(
    #     max_length = 30 ) 


    def __str__(self):
        return f"{self.user}'s profile"

    def get_absolute_url(self):
        return reverse('profiles_detail', kwargs={'pk': self.user.id})

# receivers to create/delete a Profile for every User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class PokedexPokemon(models.Model):      
    identifier = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    type1 = models.CharField(
        max_length = 10,
        choices = ELEMENT,
        default = ELEMENT[0]
    )
    type2 = models.CharField(
        max_length=10, 
        blank = True,
        null = True,
        choices = ELEMENT,
    )
    # evolution_lvl = models.IntegerField()
    # moveset = models.CharField(max_length=10) #Fix this later to be a real move set
    art_url = models.CharField(max_length=200)
    early_art_url = models.CharField(max_length=200)
    early_jp_art_url = models.CharField(max_length=200)
    icon_url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.identifier} {self.name}"


class CaughtPokemon(models.Model):
    trainer = models.ForeignKey(
        'Profile',
        on_delete = models.CASCADE
    )
    pokedex = models.ForeignKey(
        'PokedexPokemon',
        on_delete = models.CASCADE
    )
    gender = models.CharField(
        max_length = 6,
        choices = GENDER,
        blank = True,
        null = True,
    )
    nickname = models.CharField(
        max_length = 20,
        blank = True,
        null = True,
    )
    level = models.IntegerField()
    description = models.CharField(
        max_length=200,
        blank = True,
        null = True,
    )
    capture_date = models.DateField()

    def __str__(self):
        if self.nickname == None:
            return f"Lvl.{self.level} {self.pokedex.name} - {self.trainer.user}'s {self.nickname}"
        else:
            return f"Lvl.{self.level} {self.pokedex.name} - {self.trainer.user}"

class PokeField(models.Model):
    name = models.CharField(max_length=30)
    pokeMap = models.ManyToManyField('PokedexPokemon', through='PokemonList') #more accurately ref to maps table (or the intermediate table)

    def __str__(self):
        return self.name

class PokemonList(models.Model):
    pokeField = models.ForeignKey(
        'PokeField',
        on_delete = models.CASCADE
    )
    pokedexPokemon = models.ForeignKey(        
        'PokedexPokemon',
        on_delete = models.CASCADE
    )

    def getRandPokemon(self, map_id):
        pokeListObjs = self.objects.filter(pokeField=map_id)
        # for pokeObj in pokeListObjs:
        #     print(pokeObj.pokedexPokemon.name)
        randIdx = randint(0, len(pokeListObjs)-1)
        randPokemon = pokeListObjs[randIdx].pokedexPokemon
        return randPokemon

    def __str__(self):
        return f"{self.pokedexPokemon.name} on {self.pokeField}"