# Generated by Django 4.0.6 on 2022-08-11 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0009_rename_author_song_album_remove_song_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='song.song', verbose_name='comments'),
        ),
    ]
