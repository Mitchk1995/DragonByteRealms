# Generated by Django 5.0.6 on 2024-06-21 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_character_armor_class_character_background_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='armor_class',
        ),
        migrations.RemoveField(
            model_name='character',
            name='campaign',
        ),
        migrations.RemoveField(
            model_name='character',
            name='character_class',
        ),
        migrations.RemoveField(
            model_name='character',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='character',
            name='hit_points',
        ),
        migrations.RemoveField(
            model_name='character',
            name='level',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='proficiency',
        ),
    ]