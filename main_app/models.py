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
    ('♂', '♂'),
    ('♀', '♀'),
    ('', ''),
)
IMAGES = (
    (1, 'Original Suigomoto'),
    (2, 'Early Art'),
    (3, 'Early JP Art'),
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
        return f"{self.user}"

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
    min_lvl = models.IntegerField()
    evolution_lvl = models.IntegerField(
        blank = True,
        null = True,
    )
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
        # editable = False,
        on_delete = models.CASCADE
    )
    pokedex = models.ForeignKey(
        'PokedexPokemon',
        # editable = False,
        on_delete = models.CASCADE
    )
    gender = models.CharField(
        max_length = 1,
        choices = GENDER,
        blank = True,
        null = True,
    )
    nickname = models.CharField(
        max_length = 20,
        blank = True,
        null = True,
    )
    level = models.IntegerField(
        # editable = False,
        blank = True,
        null = True
    )
    description = models.CharField(
        max_length=200,
        blank = True,
        null = True,
    )
    capture_date = models.DateField(
        # editable = False,
    )
    preferred_art = models.IntegerField(
        choices = IMAGES,
        default = 1,
    )

    def __str__(self):
        if self.nickname == None:
            return f"{self.trainer.user}'s Lvl.{self.level} {self.pokedex.name}"
        else:
            return f"{self.trainer.user}'s Lvl.{self.level} {self.pokedex.name} - {self.nickname}"

    def get_absolute_url(self):
        return f"/pokebox/{self.trainer.id}"

class PokeField(models.Model):
    name = models.CharField(max_length=30)
    pokeMap = models.ManyToManyField(PokedexPokemon, through='PokemonList') #more accurately ref to maps table (or the intermediate table)

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
        # random pokemon from the list of avail pokemon in this map
        randPokemon = pokeListObjs[randIdx].pokedexPokemon
        # level = 
        return randPokemon

    def getAppropriateRandLvl(self, pokemon): 
        if pokemon.evolution_lvl == None:
            randLvl = randint(int(pokemon.min_lvl), int(pokemon.min_lvl + 20))
        else:
            randLvl = randint(pokemon.min_lvl, pokemon.evolution_lvl-1)
        return randLvl
    
    def getAppropriateGender(self, pokemon):
        pid = pokemon.identifier
        if (pid == "#029" or pid == "#030" or pid == "#031" or #nidorina family
            pid == "#113" or pid =="#115" or #chancey and khangaskhan
            pid == "#124"
           ):
            return "♀"
        elif pid == "#032" or pid == "#033" or pid == "#034": #nidorino family
            return "♂"
        elif (pid == "#081" or pid == "#082" or #mangnemite family
              pid == "#100" or pid == "#101" or #voltorb family
              pid == "#120" or pid == "#121" or #staryu family
              pid == "#132" or pid == "#137" or #ditto porygon
              pid == "#144" or pid == "#145" or pid == "#146" or #legendary birds
              pid == "#150" or pid == "#151" #mewtwo mew
             ):
            return None
        rand = randint(0,1)
        if rand == 0:
            return "♀"
        else: 
            return "♂"
    def __str__(self):
        return f"{self.pokedexPokemon.name} on {self.pokeField}"