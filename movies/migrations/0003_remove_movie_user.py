# Generated by Django 4.2 on 2023-04-14 04:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_movie_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="user",
        ),
    ]