from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import LoginForm, PokemonForm
from .models import Profile, PokedexPokemon, CaughtPokemon, PokeField, PokemonList
import urllib.parse

def debug(request):
    return render(request, 'debug.html')

## Root
def home(request):
    return render(request, 'home.html')

## Auth
def login_view(request):
    errMsg = ""
    if request.method == 'POST':
        # if POST, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    errMsg = "The account has been disabled."
            else:
                errMsg = "The username and/or password is incorrect."
    
    #If any of the above conditions fail - render a login form
    form = LoginForm()
    return render(request, 'login.html', {'form': form, 'err': errMsg})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    errMsg = ""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            errMsg = "One or more fields was invalid, please try again"
    
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'err': errMsg})

## Profiles Views
class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['bio', 'location']        

@login_required
def profiles_index(request):
    profiles = Profile.objects.order_by('user')
    return render(request, 'profiles/index.html', {'profiles': profiles})

@login_required
def profiles_detail(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, 'profiles/detail.html', {'profile': profile})

## Maps Views
def maps_index(request):
    poke_fields_list = PokeField.objects.all()
    return render(request, 'maps/index.html', {"pokefields": poke_fields_list})

@login_required
def maps_detail(request, map_id):
    pokemon = PokemonList.getRandPokemon(PokemonList, map_id)
    lvl = PokemonList.getAppropriateRandLvl(PokemonList, pokemon)
    gender = PokemonList.getAppropriateGender(PokemonList, pokemon)
    user_id = request.user.id
    print(pokemon.id)
    if gender:
        catch_url = f"/pokebox/{user_id}/create?lvl={str(lvl)}&gender={str(gender)}&pokedex_id={pokemon.id}"
    else:
        catch_url = f"/pokebox/{user_id}/create?lvl={str(lvl)}&pokedex_id={pokemon.id}"

    return render(request, 'maps/detail.html', {'pokemon': pokemon, 'gender': gender, 'randLvl': lvl, 'catch_url': catch_url})

def caughtPokemonCreate(request, pk):
    my_kwargs = {
        'lvl': request.GET.get('lvl'),
        'gender': request.GET.get('gender'),
        'pokedex_id': request.GET.get('pokedex_id'),
    }

    errMsg = ""
    #if user submitting form
    if request.method == 'POST': 
        form = PokemonForm(request.POST)
        if form.is_valid():
            # saves the form + data to db as a CaughtPokemon
            # pokeForm = form.save()
            form.save()
            profile = Profile.objects.get(pk=pk)
            url = f"/pokebox/{pk}/"
            return redirect(url, {'profile': profile})
        else:
            errMsg = "One or more fields was invalid, please try again"
    #if user receiving a brand new form
    form = PokemonForm(initial = {
        'trainer': pk, 
        'pokedex': my_kwargs.get('pokedex_id'),
        'gender': my_kwargs.get('gender'),
        'level': my_kwargs.get('lvl'),
        'preferred_art': 1
    })
    return render(request, 'main_app/caughtpokemon_form.html', {'form': form, 'err': errMsg})



## Pokebox Views
@method_decorator(login_required, name='dispatch')
class PokeboxList(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'pokebox/index.html'


@login_required
def pokebox_detail(request, pk):
    pokemons = CaughtPokemon.objects.filter(trainer=pk)
    return render(request, 'pokebox/detail.html', {'caughtPokemons': pokemons})

@login_required
def solo_detail(request, user_id, pokemon_id):
    pokemon = CaughtPokemon.objects.get(id = pokemon_id)
    print(f"poke id: {pokemon_id} | user id {user_id}")
    # print(pokemon)
    trainer = pokemon.trainer 
    print(f"poke id: {pokemon.id} | {pokemon} | {trainer}")
    return render(request, 'pokebox/solo_detail.html', {'pokemon': pokemon, 'trainer_id': trainer.id})

@method_decorator(login_required, name='dispatch')
class CaughtPokemonUpdate(UpdateView):
    model = CaughtPokemon
    fields = ['gender', 'nickname', 'description', 'preferred_art']
    pk_url_kwarg = 'pokemon_id' 
# def caughtPokemon_Update(request, user_id, pokemon_id):
#     form = PokemonForm(request.POST)


@method_decorator(login_required, name='dispatch')
class CaughtPokemonDelete(DeleteView):
    model = CaughtPokemon
    # url = f"/pokebox/{pk}"
    pk_url_kwarg = 'pokemon_id' 
    success_url = "/"

## Pokedex View
def pokedex_index(request):
    return render(request, 'pokedex/index.html', {'pokedex': PokedexPokemon.objects.all()})

def pokedex_detail(request, pk):
    pokedex_pokemon = PokedexPokemon.objects.get(id=pk)
    return render(request, 'pokedex/detail.html', {'pokemon': pokedex_pokemon})

## Leaderboard View
def leaderboard(request):
    return render(request, 'index.html')
