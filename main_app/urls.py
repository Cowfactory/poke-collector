from django.urls import path
from . import views

urlpatterns = [
    # Main Menu
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),

    # Maps
    path('maps/', views.maps_index, name='maps_index'),
    path('maps/<int:map_id>/', views.maps_detail, name="maps_detail"),

    #Leaderboard
    path('leaderboard/', views.leaderboard, name='leaderboard'),
   
    # Profile / Caught Pokemon 
    path('pokebox/', views.pokebox_index, name="pokebox_index"),
    path('pokebox/<int:pk>/', views.pokebox_detail, name="pokebox_detail"),
    path('pokebox/create/', views.CaughtPokemonCreate.as_view(), name="pokemon_create"),

    # Pokedex
    path('pokedex/', views.pokedex, name="pokedex"),

]