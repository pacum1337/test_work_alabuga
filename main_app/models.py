from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField("Название", max_length=255)
    author = models.ForeignKey(User, models.CASCADE, verbose_name='Автор')
    content = models.TextField("Контент записи", blank=True)
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)
    tags = models.ManyToManyField(Tag, verbose_name="Теги", related_name='posts', blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='likes')

    def __str__(self):
        return f'{self.post} - {self.user}'


class Favorite(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='favorites')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='favorites')

    def __str__(self):
        return f'{self.post} - {self.user}'
