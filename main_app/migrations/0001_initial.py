# Generated by Django 2.1.2 on 2018-10-18 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaughtPokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=6, null=True)),
                ('nickname', models.CharField(blank=True, max_length=20, null=True)),
                ('level', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('capture_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PokedexPokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=20)),
                ('type1', models.CharField(choices=[('Normal', 'Normal'), ('Fighting', 'Fighting'), ('Flying', 'Flying'), ('Poison', 'Poison'), ('Ground', 'Ground'), ('Rock', 'Rock'), ('Bug', 'Bug'), ('Ghost', 'Ghost'), ('Fire', 'Fire'), ('Water', 'Water'), ('Grass', 'Grass'), ('Electric', 'Electric'), ('Psychic', 'Psychic'), ('Ice', 'Ice'), ('Dragon', 'Dragon')], default=('Normal', 'Normal'), max_length=10)),
                ('type2', models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Fighting', 'Fighting'), ('Flying', 'Flying'), ('Poison', 'Poison'), ('Ground', 'Ground'), ('Rock', 'Rock'), ('Bug', 'Bug'), ('Ghost', 'Ghost'), ('Fire', 'Fire'), ('Water', 'Water'), ('Grass', 'Grass'), ('Electric', 'Electric'), ('Psychic', 'Psychic'), ('Ice', 'Ice'), ('Dragon', 'Dragon')], max_length=10, null=True)),
                ('min_lvl', models.IntegerField()),
                ('evolution_lvl', models.IntegerField(blank=True, null=True)),
                ('art_url', models.CharField(max_length=200)),
                ('early_art_url', models.CharField(max_length=200)),
                ('early_jp_art_url', models.CharField(max_length=200)),
                ('icon_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PokeField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokeField', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.PokeField')),
                ('pokedexPokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.PokedexPokemon')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pokefield',
            name='pokeMap',
            field=models.ManyToManyField(through='main_app.PokemonList', to='main_app.PokedexPokemon'),
        ),
        migrations.AddField(
            model_name='caughtpokemon',
            name='pokedex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.PokedexPokemon'),
        ),
        migrations.AddField(
            model_name='caughtpokemon',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profile'),
        ),
    ]
