from django.contrib import admin
from .models import Tag, Post, Like, Favorite

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Favorite)
