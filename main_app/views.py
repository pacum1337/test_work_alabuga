from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tag, Post, Like, User, Favorite
from .serializers import TagSerializer, PostSerializer, LikeSerializer, FavoriteSerializer


class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostSearchView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        try:
            return Post.objects.all().order_by(self.kwargs['filter'])
        except:
            raise Http404


class LikeRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(user_id=self.kwargs['pk'])


class LikeCreateView(APIView):
    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            Like.objects.update_or_create(user_id=request.data['user'], post_id=request.data['post'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoriteRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user_id=self.kwargs['pk'])


class FavoriteCreateView(APIView):
    def post(self, request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            Favorite.objects.update_or_create(user_id=request.data['user'], post_id=request.data['post'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
