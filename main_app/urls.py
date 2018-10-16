from django.urls import path
from . import views

urlpatterns = [
    # Main Menu
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    # Pokedex
    path('pokedex/', views.pokedex, name='pokedex'),
    # Leaderboard
    path('leaderboard/', views.leaderboard, name='leaderboard'),

    # Maps
    path('maps/', views.maps_index, name='maps_index'),
    path('maps/<int:map_id>/', views.maps_detail, name='maps_detail'),

    # Caught Pokemon
    path('pokemon/', views.caughtPokemons_index, name='caughtPokemons_index'),
    path('pokemon/<int:pk>', views.caughtPokemons_detail, name='caughtPokemons_detail'),
    path('pokemon/create/', views.CaughtPokemonCreate.as_view(), name='caughtPokemons_create'),

    # User's Pokemon Box (Pokebox) 
    path('pokebox/', views.PokeboxList.as_view(), name='pokebox_index'),
    path('pokebox/<int:pk>/', views.PokeboxDetail.as_view(), name='pokebox_detail'),
    
 

]