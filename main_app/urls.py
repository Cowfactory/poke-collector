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
    path('profiles/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profiles_update'),   

    # Maps
    path('maps/', views.maps_index, name='maps_index'),
    path('maps/<int:map_id>/', views.maps_detail, name='maps_detail'),

    # User's Pokemon Box (Pokebox) 
    path('pokebox/', views.PokeboxList.as_view(), name='pokebox_index'),
    path('pokebox/<int:pk>/', views.pokebox_detail, name='pokebox_detail'),
    path('pokebox/<int:pk>/create/', views.caughtPokemonCreate, name='caughtPokemon_create'),
    path('pokebox/<int:user_id>/<int:pokemon_id>/', views.solo_detail, name='solo_detail'),
    path('pokebox/<int:pk>/<int:pokemon_id>/update/', views.CaughtPokemonUpdate.as_view(), name='caughtPokemon_update'),
    path('pokebox/<int:pk>/<int:pokemon_id>/delete/', views.CaughtPokemonDelete.as_view(), name='caughtPokemon_delete'),
    
    # Pokedex
    path('pokedex/', views.pokedex_index, name='pokedex_index'),
    path('pokedex/<int:pk>/', views.pokedex_detail, name='pokedex_detail'),

    # Leaderboard
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
