from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import LoginForm
from .models import Profile, PokedexPokemon, CaughtPokemon

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
            return redirect('index')
        else:
            errMsg = "One or more fields was invalid, please try again"
    
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'err': errMsg})

## Profiles Views
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
    return render(request, 'maps/index.html')

def maps_detail(request):
    return render(request, 'maps/detail.html')



class CaughtPokemonCreate(CreateView):
    model = CaughtPokemon
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/')

## Pokebox Views
class PokeboxList(ListView):
        model = Profile
        context_object_name = 'profiles'
        template_name = 'pokebox/index.html'

        # def get_context_data(self, **kwargs):
        #     # Call the base implementation first to get a context
        #     context = super().get_context_data(**kwargs)
        #     # Add in a QuerySet of all the Pokebox belonging to the user
        #     thing = []
        #     for user in User.objects.all():
        #         thing.append())

        #     all_pokemon = CaughtPokemon.objects.all()
        #     for pokemon in all_pokemon:
        #         thing[pokemon.trainer_id] 

        #     context['user'] =
        
        #     return context

@login_required
def pokebox_detail(request, pk):
    pokemons = CaughtPokemon.objects.filter(trainer=pk)
    print(pokemons)
    return render(request, 'pokebox/detail.html', {'caughtPokemons': pokemons})



## Pokedex View
def pokedex(request):
    return render(request, 'pokedex.html', {'pokedex': PokedexPokemon.objects.all()})

def pokedex_detail(request):
    return render(request, 'index.html')

## Leaderboard View
def leaderboard(request):
    return render(request, 'index.html')


## Caught Pokemon Views
# @login_required
# def caughtPokemons_index(request):
#     pokemons = CaughtPokemon.objects.all()
#     return render(request, 'pokemon/index.html', {'pokemons': pokemons})

# @login_required
# def caughtPokemons_detail(request, pk):
#     pokemon = CaughtPokemon.objects.get(pk=pk)
#     return render(request, 'pokemon/detail.html', {'pokemon': pokemon})