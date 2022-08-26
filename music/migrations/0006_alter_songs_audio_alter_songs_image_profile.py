# Generated by Django 4.0.5 on 2022-08-24 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0005_alter_songs_audio_alter_songs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='audio',
            field=models.FileField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(upload_to='media')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]