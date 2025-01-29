from django.contrib import admin
from .models import Article, Category
from django.db import models

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)