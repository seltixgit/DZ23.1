# Generated by Django 5.0.6 on 2024-07-23 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='Изображение'),
        ),
    ]
