from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Blog, BlogAdmin)
