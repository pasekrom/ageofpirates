# Generated by Django 4.1.2 on 2022-10-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ageofpirates', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='odkaz_statistika',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='odkaz_steam',
            new_name='statistika',
        ),
        migrations.AddField(
            model_name='player',
            name='steam',
            field=models.TextField(default='asd'),
            preserve_default=False,
        ),
    ]
