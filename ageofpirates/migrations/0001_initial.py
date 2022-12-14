# Generated by Django 4.1.2 on 2022-10-05 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Civilization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nazev', models.TextField()),
                ('emblem', models.TextField()),
            ],
            options={
                'verbose_name': 'Civilizace',
                'verbose_name_plural': 'Civilizace',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('jmeno', models.TextField()),
                ('popis', models.TextField()),
                ('odkaz_statistika', models.TextField()),
                ('odkaz_steam', models.TextField()),
            ],
            options={
                'verbose_name': 'Hráč',
                'verbose_name_plural': 'Hráči',
            },
        ),
    ]
