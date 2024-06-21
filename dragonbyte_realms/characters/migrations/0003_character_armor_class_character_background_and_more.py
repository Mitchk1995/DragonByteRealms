# Generated by Django 5.0.6 on 2024-06-21 01:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='armor_class',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='background',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='charisma',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='constitution',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='dexterity',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='hit_points',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='wisdom',
            field=models.IntegerField(default=10),
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(default=1)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='characters.character')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('proficiency', models.BooleanField(default=False)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='characters.character')),
            ],
        ),
    ]