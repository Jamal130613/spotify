# Generated by Django 4.0.6 on 2022-08-12 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('song', '0011_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL, verbose_name='ratings'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL, verbose_name='favorites')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='song.song', verbose_name='Song')),
            ],
        ),
    ]