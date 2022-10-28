from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=68)
    price = models.ImageField(max_length=60)
    image = models.CharField(max_length=150)
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    # TODO: Добавьте требуемые поля
    pass
