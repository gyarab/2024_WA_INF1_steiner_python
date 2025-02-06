from django.contrib import admin
from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    #list_filter = ['category']
    date_hierarchy = 'published'
    search_fields = ['title', 'perex', 'text']

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

