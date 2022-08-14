from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Category(models.Model):
    title = models.SlugField(primary_key=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='songs')
    artist = models.CharField(max_length=50) 
    title = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE,
                                related_name='music')
    duration = models.CharField(max_length=20)
    country = CountryField()
    created_at = models.DateField()
    photo = models.ImageField(upload_to='photos', blank=True)
    audio_file = models.FileField(upload_to='songs')
    audio_link = models.CharField(max_length=200)

    class Meta:
        db_table='song'

    def __str__(self):
        return f'{self.title}, {self.artist}'


class Like(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='likes',
                              verbose_name='Like owner')
    song = models.ForeignKey(Song,
                                on_delete=models.CASCADE,
                                related_name='likes',
                                verbose_name='Song')
    like = models.BooleanField('like', default=True)

    def __str__(self):
        return f'{self.song} {self.like}'


class Comment(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='comments',
                              verbose_name='comments')
    song = models.ForeignKey(Song,
                                on_delete=models.CASCADE,
                                related_name='comments',
                                verbose_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} - {self.song}'


class Rating(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='ratings',
                              verbose_name='ratings')
    song = models.ForeignKey(Song,
                                on_delete=models.CASCADE,
                                related_name='ratings',
                                verbose_name='Song')
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ], default=1
    )

    def __str__(self):
        return f'{self.song} - {self.rating}'


class Favorite(models.Model):
    owner = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='favorites',
                            verbose_name='favorites')
    song = models.ForeignKey(Song,
                                on_delete=models.CASCADE,
                                related_name='favorites',
                                verbose_name='Song')

    def __str__(self):
        return f'{self.owner} - {self.song}'
