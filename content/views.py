from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse
from django.urls import reverse
import json
from .models import Article, Category

# Create your views here.
def articles(request):
    articles = Article.objects.all()
    categories = Category.objects.all()  # Získání všech kategorií

    context = {
        'articles': articles,
        'categories': categories,  # Přidání kategorií do kontextu
    }
    return render(request, 'content/articles.html', context)

def article(request, id):
    article = Article.objects.get(id=id)
    
    return render(request, 'content/article.html', {'article': article})

def category(request, id):
    category = Category.objects.get(id=id)

    articles = category.articles.all()

    
    return render(request, 'content/category.html', {'category':category, 'articles': articles})
    
