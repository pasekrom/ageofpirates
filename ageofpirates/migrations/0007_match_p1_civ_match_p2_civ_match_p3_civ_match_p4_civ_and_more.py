# Generated by Django 4.1.2 on 2022-10-05 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ageofpirates', '0006_alter_match_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='p1_civ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player1_civ', to='ageofpirates.civilization'),
        ),
        migrations.AddField(
            model_name='match',
            name='p2_civ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player2_civ', to='ageofpirates.civilization'),
        ),
        migrations.AddField(
            model_name='match',
            name='p3_civ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player3_civ', to='ageofpirates.civilization'),
        ),
        migrations.AddField(
            model_name='match',
            name='p4_civ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player4_civ', to='ageofpirates.civilization'),
        ),
        migrations.AddField(
            model_name='match',
            name='p5_civ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player5_civ', to='ageofpirates.civilization'),
        ),
        migrations.AddField(
            model_name='match',
            name='p6_civ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player6_civ', to='ageofpirates.civilization'),
        ),
        migrations.AddField(
            model_name='match',
            name='p7_civ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player7_civ', to='ageofpirates.civilization'),
        ),
        migrations.AddField(
            model_name='match',
            name='p8_civ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player8_civ', to='ageofpirates.civilization'),
        ),
    ]
