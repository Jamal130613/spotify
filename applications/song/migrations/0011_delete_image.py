# Generated by Django 4.0.6 on 2022-08-11 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0010_alter_comment_song'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
