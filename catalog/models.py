from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='image', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='Category')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего изменения')
    manufactured_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата производства продукта')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
