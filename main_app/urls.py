from django.urls import path
from .views import TagView, PostView, LikeRetrieveView, FavoriteRetrieveView, LikeCreateView, FavoriteCreateView, \
    PostSearchView

urlpatterns = [
    path('tags/', TagView.as_view()),
    path('posts/', PostView.as_view()),
    path('posts/<slug:filter>/', PostSearchView.as_view()),
    path('likes/create/', LikeCreateView.as_view()),
    path('likes/<int:pk>/', LikeRetrieveView.as_view()),
    path('favorites/create/', FavoriteCreateView.as_view()),
    path('favorites/<int:pk>/', FavoriteRetrieveView.as_view()),
]
