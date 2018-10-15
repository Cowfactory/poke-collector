from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import LoginForm
from .models import PokedexPokemon, CaughtPokemon

# Create your views here.
def index(request):
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

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

### LEADERBOARD ###
def leaderboard(request):
    return render(request, 'index.html')

### PROFILE ###
@login_required
def profile(request):
    return render(request, 'profile.html')

### MAPS ###
def maps_index(request):
    return render(request, 'maps/index.html')

def maps_detail(request):
    return render(request, 'maps/detail.html')

### POKEMON BOX ###
class CaughtPokemonCreate(CreateView):
    model = CaughtPokemon
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/index.html')

@login_required
def pokebox_index(request):
    user = request.user
    pokemons = CaughtPokemon.objects.filter(trainer_id=user.id)
    return render(request, 'pokebox/index.html', {'pokemons': pokemons})

@login_required
def pokebox_detail(request, pk):
    pokemon = CaughtPokemon.objects.get(pk=pk)
    return render(request, 'pokebox/detail.html', {'pokemon': pokemon})



### POKEDEX
def pokedex(request):
    return render(request, 'pokedex.html', {'pokedex': PokedexPokemon.objects.all()})
    

