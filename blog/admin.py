from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content', 'photo', 'created_at', 'is_published', 'views')
    search_fields = ('title', 'is_published')

def my_media(data):
    if data:
        return f'/media/photo/{data}'
    return f'/media/photo/empty.pic.jpg'
