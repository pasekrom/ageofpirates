# Generated by Django 4.1.2 on 2022-10-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ageofpirates', '0008_remove_player_popis_alter_civilization_emblem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='pocet_tymu',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
