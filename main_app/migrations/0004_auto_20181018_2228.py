# Generated by Django 2.1.2 on 2018-10-18 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20181018_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caughtpokemon',
            name='preferred_img',
            field=models.IntegerField(choices=[('Original Suigomoto', 1), ('Early Art', 2), ('Early JP Art', 3)], default=1),
            preserve_default=False,
        ),
    ]
