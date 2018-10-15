from django.urls import path
from . import views

urlpatterns = [
    # Main Menu
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),

    # Maps
    path('maps/', views.maps_index, name='maps_index'),
    path('maps/<int:map_id>', views.maps_detail, name="maps_detail"),

    # Pokemon 
    path('pokemon/', views.pokemon_index, name="pokemon_index"),
    path('pokemon/<int:pk>', views.pokemon_detail, name="pokemon_detail"),
    path('pokemon/create', views.PokemonCreate.as_view(), name="pokemon_create"),

]