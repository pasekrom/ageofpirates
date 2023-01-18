# Generated by Django 4.1.2 on 2023-01-18 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ageofpirates', '0031_rename_qf_tournamentmatch_f_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('umisteni', models.PositiveSmallIntegerField()),
                ('text', models.TextField()),
                ('hrac', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ageofpirates.player')),
            ],
            options={
                'verbose_name': 'Ocenění',
                'verbose_name_plural': 'Ocenění',
            },
        ),
    ]
