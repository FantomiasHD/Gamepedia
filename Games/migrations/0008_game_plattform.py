# Generated by Django 3.0.7 on 2020-06-29 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0007_remove_game_plattform'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='plattform',
            field=models.ManyToManyField(to='Games.Plattform'),
        ),
    ]
