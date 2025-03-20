from django.contrib import admin
from .models import Article, Category, Biom, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'version', 'lastUpdate']
    list_display_links = ['id', 'title']
    list_filter = ['categories', 'biom']  # Opravený filtr pro nové ManyToMany pole
    date_hierarchy = 'lastUpdate'  # Opravený název pole
    search_fields = ['title', 'zakladniInfo', 'dodatkovyText', 'vyroba', 'version']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Biom)
admin.site.register(Category)
admin.site.register(Comment)

