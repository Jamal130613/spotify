from django.contrib import admin
from applications.song.models import Category, Song


class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'duration', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['title']


admin.site.register(Category)
admin.site.register(Song, SongAdmin)