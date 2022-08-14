from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views

router = DefaultRouter()
router.register('category', CategoryView)
router.register('comment', CommentView)
router.register('',SongView)

app_name = "Song"

urlpatterns = [
    path('', include(router.urls)),
    path("index", views.index, name="index"),
]



