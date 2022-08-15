from django.shortcuts import render, redirect
from .models import Category, Like, Song, Favorite, Playlist
from .serializers import *
from .permissions import CustomIsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.core.paginator import Paginator


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomIsAdmin]


class SongView(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    search_fields = ['name', 'artist']
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'artist', 'category']
    search_fields =['title', 'artist']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['GET'])
    def songs(self,request,pk=None):
        queryset = self.get_queryset()
        queryset=queryset.filter(owner=request.user)
        serializer=SongSerializer(queryset,many=True)
        return Response(serializer.data,status=200)

    @action(methods=['POST'], detail=True)
    def like(self,request, pk, *args, **kwargs):
     try:

        like_object, _ =  Like.objects.get_or_create(owner=request.user,song_id=pk)
        like_object.like = not like_object.like
        like_object.save()
        status = 'liked'

        if like_object.like:
            return Response({'status': status})
        status = 'unliked'
        return Response({'status': status})
     except:
         return Response('This song does not exist!')

    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        serializers = RatingSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        object, _ = Rating.objects.get_or_create(song_id=pk,
                                              owner=request.user)
        object.rating = request.data['rating']
        object.save()
        return Response(request.data, status=201)

    @action(methods=['POST'], detail=True)
    def favorite(self, request, pk, *args, **kwargs):
        favorite, _ = Favorite.objects.get_or_create(owner=request.user, song_id=pk)
        if not _:
            favorite.delete()
            return Response('Removed from favorites')
        else:
            favorite.save()
            return Response('Added to favorites!')

    @action(methods=['POST'], detail=True)
    def playlist(self, request, pk, *args, **kwargs):
        playlist, _ = Playlist.objects.get_or_create(owner=request.user, song_id=pk)
        if not _:
            playlist.delete()
            return Response('This song was deleted from your playlist')
        else:
            playlist.save()
            return Response('This song was added to your playlist')

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'like':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]

        return [p() for p in permissions]


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)