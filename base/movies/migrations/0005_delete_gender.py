# Generated by Django 5.0.3 on 2024-05-14 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movies_genre'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gender',
        ),
    ]