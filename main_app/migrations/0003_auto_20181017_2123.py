# Generated by Django 2.1.2 on 2018-10-17 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_pokefield'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='pokefield',
            name='pokemon_list',
        ),
        migrations.AddField(
            model_name='pokemonlist',
            name='pokeField',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.PokeField'),
        ),
        migrations.AddField(
            model_name='pokemonlist',
            name='pokedexPokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.PokedexPokemon'),
        ),
        migrations.AddField(
            model_name='pokefield',
            name='pokeMap',
            field=models.ManyToManyField(through='main_app.PokemonList', to='main_app.PokedexPokemon'),
        ),
    ]
