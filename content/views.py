from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse
from django.http import HttpResponseRedirect as HTTPResponseRedirect
from django.urls import reverse
import json
from .models import Article, Category, Comment
from .forms import CommentForm
from django.contrib.auth import authenticate, login, logout 
from .forms import LoginForm, LogoutForm
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.
def articles(request):
    articles = Article.objects.all()
    categories = Category.objects.all()  # Získání všech kategorií

    context = {
        'articles': articles,
        'categories': categories,  # Přidání kategorií do kontextu
    }

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = Comment()
            comment.name = data['name']
            comment.text = data['text']
            comment.article = article
            comment.ip = request.META.get('REMOTE_ADDR')
            comment.user_agent = request.META.get('HTTP_USER_AGENT')
            comment.save()
            return HTTPResponseRedirect(reverse('content:article', args=[id]))
        
    if request.method == 'GET' and 'vote' in request.GET:
        cookiename=f'voted_{article.id}'
        if cookiename in request.COOKIES:
            return HTTPResponseRedirect(reverse('content:article', args=[id]))
        
        vote = int(request.GET['vote'])
        if vote <= 5 and vote >= 1:
            article.vote_sum += vote
            article.vote_count += 1
            article.save()

            response = HTTPResponseRedirect(reverse('content:article', args=[id]))
            response.set_cookie(cookiename, '1')
            return response
        
    return render(request, 'content/articles.html', context)

def article(request, id):
    article = Article.objects.get(id=id)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = Comment()
            comment.name = data['name']
            comment.text = data['text']
            comment.article = article
            comment.ip = request.META.get('REMOTE_ADDR') 
            comment.user_agent = request.META.get('HTTP_USER_AGENT')
            comment.save()

            return HTTPResponseRedirect(reverse('content:article', args=[id]))


    if request.method == 'GET' and 'vote' in request.GET:
        cookiename=f'voted_{article.id}'
        if cookiename in request.COOKIES:
            return HTTPResponseRedirect(reverse('content:article', args=[id]))
        
        vote = int(request.GET['vote'])
        if vote <= 9 and vote >= 1:
            article.vote_sum += vote
            article.vote_count += 1
            article.save()

            response = HTTPResponseRedirect(reverse('content:article', args=[id]))
            
            response.set_cookie(cookiename, '1')
            return response
    
    return render(request, 'content/article.html', {'article': article, 'form': form})

def category(request, id):
    category = Category.objects.get(id=id)

    articles = category.articles.all()
    
    return render(request, 'content/category.html', {'category':category, 'articles': articles})

def login_view(request):
    form = LoginForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HTTPResponseRedirect(reverse('content:login'))
        else:
            form.add_error(None, 'Neplatné přihlašovací údaje')
    else:
        form = LogoutForm()
        return render(request, 'content/login.html', {'form': form, 'user': request.user})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('content:login')
    else:
        # Můžeš zobrazit formulář pro potvrzení odhlášení
        form = LogoutForm()
        return render(request, 'content/logout.html', {'form': form})

    
