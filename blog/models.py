from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок", help_text="Введите заголовок",)
    slug = models.CharField(max_length=50, verbose_name="Ссылка", help_text="Введите ссылку",)
    content = models.TextField(verbose_name="Содержимое", help_text="Введите содержимое", blank=True, null=True)
    photo = models.ImageField(upload_to="photo", blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров",
                                        help_text="Укажите количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
