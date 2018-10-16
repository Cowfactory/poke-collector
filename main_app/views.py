from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import LoginForm
from .models import PokedexPokemon, CaughtPokemon

## Main Menu Views
def index(request):
    return render(request, 'index.html')

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

@login_required
def profile(request):
    return render(request, 'profile.html')

## Pokedex View
def pokedex(request):
    return render(request, 'pokedex.html', {'pokedex': PokedexPokemon.objects.all()})

## Leaderboard View
def leaderboard(request):
    return render(request, 'index.html')

## Maps Views
def maps_index(request):
    return render(request, 'maps/index.html')

def maps_detail(request):
    return render(request, 'maps/detail.html')

## Caught Pokemon Views
@login_required
def caughtPokemons_index(request):
    user = request.user
    pokemons = CaughtPokemon.objects.filter(trainer_id=user.id)
    return render(request, 'pokebox/index.html', {'pokemons': pokemons})

@login_required
def caughtPokemons_detail(request, pk):
    pokemon = CaughtPokemon.objects.get(pk=pk)
    return render(request, 'pokebox/detail.html', {'pokemon': pokemon})

class CaughtPokemonCreate(CreateView):
    model = CaughtPokemon
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/index.html')

## Pokebox Views
# @login_required
# def pokebox_index(request):
#     user = request.user
#     pokemons = CaughtPokemon.objects.filter(trainer_id=user.id)
#     return render(request, 'pokebox/index.html', {'pokemons': pokemons})

# def pokebox_detail(request, pk):
#     pokemons = CaughtPokemon.objects.filter(pk=pk)
#     return render(request, 'pokebox/detail.html', {'pokemons': pokemons})

class PokeboxList(ListView):
    model = CaughtPokemon
    context_object_name = 'pokebox'
    template_name = 'pokebox/index.html'

class PokeboxDetail(DetailView):
    model = CaughtPokemon
    context_object_name = 'pokebox' # my custom template var name
    template_name = 'pokebox/detail.html' # specify where the template is located in fs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['pokebox'] = CaughtPokemon.objects.filter(trainer_id=self.kwargs['pk'])
        return context





