# Generated by Django 4.0.4 on 2022-04-19 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_genre_remove_movie_actors_count_alter_movie_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='media/movies_thumbnails'),
        ),
    ]