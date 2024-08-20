from django.db import models

from users.models import User


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='image', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category,
                                 on_delete=models.RESTRICT,
                                 verbose_name='Категория',
                                 help_text='Введите категорию товара')
    price = models.PositiveIntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')
    author = models.ForeignKey(User, verbose_name="Автор", blank=True, null=True, on_delete=models.SET_NULL,
                               related_name='users')
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [
            ('can_edit_product_description', 'Can edit product description'),
            ('can_edit_product_category', 'Can edit product category'),
            ('can_cancel_publication', 'Can cancel publication of product'),
        ]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продукт",
    )
    version_number = models.CharField(
        max_length=10,
        verbose_name="Номер версии",
        null=True,
        blank=True,
    )
    version_name = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        null=True,
        blank=True,
    )
    indicates_current_version = models.BooleanField(
        default=False,
        verbose_name="Активная версия",
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"

    def __str__(self):
        return f"{self.version_name} - {self.version_number}, {self.product}, {self.indicates_current_version}"
