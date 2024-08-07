from django.db import models


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

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

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
