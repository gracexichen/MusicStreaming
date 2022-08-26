# Generated by Django 4.0.5 on 2022-08-25 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_songs_audio_alter_songs_image_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('song', models.ManyToManyField(to='music.songs')),
            ],
        ),
    ]