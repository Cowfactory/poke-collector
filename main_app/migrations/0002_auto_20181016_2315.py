# Generated by Django 2.1.2 on 2018-10-16 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caughtpokemon',
            old_name='pokedex_id',
            new_name='pokedex',
        ),
        migrations.RenameField(
            model_name='pokedexpokemon',
            old_name='pokedex_id',
            new_name='identifier',
        ),
    ]