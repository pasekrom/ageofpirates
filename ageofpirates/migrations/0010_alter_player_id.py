# Generated by Django 4.1.2 on 2022-10-05 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ageofpirates', '0009_match_pocet_tymu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
