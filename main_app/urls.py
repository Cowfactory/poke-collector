from django.urls import path
from . import views

urlpatterns = [
    path('debug/', views.debug, name='debug'),

    # Root
    path('', views.home, name='home'),

    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    
    # Profiles
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<int:pk>/', views.profiles_detail, name='profiles_detail'),   

    # Maps
    path('maps/', views.maps_index, name='maps_index'),
    path('maps/<int:map_id>/', views.maps_detail, name='maps_detail'),

    # User's Pokemon Box (Pokebox) 
    path('pokebox/', views.PokeboxList.as_view(), name='pokebox_index'),
    path('pokebox/<int:pk>/', views.pokebox_detail, name='pokebox_detail'),
    # path('pokebox/<int:pk>/<int:pk>', views.PokeboxDetail.as_view(), name='single pokemon'),
    path('pokebox/<int:pk>/create/', views.CaughtPokemonCreate.as_view(), name='caughtPokemon_create'),
    
    # Pokedex
    path('pokedex/', views.pokedex, name='pokedex'),
    path('pokedex/<int:pk>/', views.pokedex_detail, name='pokedex_detail'),
    
    # Moves
    # path('moves/', views.moves_index, name='moves_index'),
    # path('moves/<int:pk>', views.moves_detail, name='moves_detail'),

    # Leaderboard
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]

    # Caught Pokemon
    # path('pokemon/', views.caughtPokemons_index, name='caughtPokemons_index'),
    # path('pokemon/<int:pk>', views.caughtPokemons_detail, name='caughtPokemons_detail'),
    # path('pokemon/create/', views.CaughtPokemonCreate.as_view(), name='caughtPokemons_create'),