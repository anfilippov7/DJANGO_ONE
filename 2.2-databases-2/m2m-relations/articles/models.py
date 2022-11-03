from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    # tags = models.ManyToManyField('TopicsArticle', max_length=20, related_name='tag')
    cat_id = models.ManyToManyField('TopicsArticle', related_name='tag')


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class TopicsArticle(models.Model):
    cat_id = models.ManyToManyField(Article, related_name='tag2')
    topics = models.ForeignKey(Article, on_delete=models.PROTECT, null=True)
    tags = models.ManyToManyField(Article, max_length=50, related_name='tag', verbose_name='Раздел')
    # tags = models.CharField(max_length=256, verbose_name='Раздел')
    main = models.BooleanField(default=False, verbose_name='Основной')
    delete = models.BooleanField(default=False, verbose_name='Удалить?')

    class Meta:
        verbose_name = 'Тематика Статьи'
        verbose_name_plural = 'ТЕМАТИКИ СТАТЬИ'

    # def __str__(self):
    #     return self.tags

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     category = models.CharField(max_length=50)

# class Order(models.Model):
#     pass
#
# class OrderPosition(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='positions')
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions')
#     quantity = models.IntegerField()