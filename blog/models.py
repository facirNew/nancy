from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    short_view = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    content = models.TextField(blank=True, verbose_name='Содержание')
    photo = models.ImageField(upload_to="img/%Y/%m/%d/", blank=True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    tags = models.ManyToManyField('Tags', verbose_name='Тэги')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['time_create']


class Tags(models.Model):
    name = models.CharField(max_length=32, db_index=True, verbose_name='Тег')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})
