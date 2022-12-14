# Generated by Django 4.1.2 on 2022-10-10 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ageofpirates', '0013_tournament'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='pocet_hracu',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='vitez',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ageofpirates.player'),
        ),
    ]
