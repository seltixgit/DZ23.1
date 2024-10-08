# Generated by Django 4.2.2 on 2024-08-14 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0009_alter_version_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='author',
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
