from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.ManyToManyField(Article, related_name='tag', through='ArticleScope')
    name = models.CharField(max_length=256, verbose_name='Тэг')

    class Meta:
        verbose_name = 'Тэги'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class ArticleScope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tags', verbose_name='Раздел')
    main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика Статьи'
        verbose_name_plural = 'ТЕМАТИКИ СТАТЬИ'







