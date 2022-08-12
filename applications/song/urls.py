from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('category', CategoryView)
router.register('comment', CommentView)
router.register('',SongView)


urlpatterns = [
    path('', include(router.urls))
]