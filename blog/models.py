from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    content = models.TextField('Описание', blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
