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
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from .models import Comment  # nebo Review, podle pojmenování
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden



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
            comment.user = request.user if request.user.is_authenticated else None
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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('content:login'))
            else:
                messages.warning(request, 'Neplatné přihlašovací údaje.')
    else:
        form = LoginForm()

    return render(request, 'content/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('content:login')
    else:
        # Můžeš zobrazit formulář pro potvrzení odhlášení
        form = LogoutForm()
        return render(request, 'content/logout.html', {'form': form})

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'content/register.html', {'register_form': form})

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 != password2:
                form.add_error('password2', 'Hesla se neshodují')
                return render(request, 'content/register.html', {'register_form': form})

            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()

            return redirect(reverse('content:login'))
        else:
            return render(request, 'content/register.html', {'register_form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Uživatel může smazat, pokud je autor nebo má oprávnění
    if request.user == comment.user or request.user.has_perm('content.delete_comment'):
        comment.delete()
        return redirect(request.META.get('HTTP_REFERER', 'content:articles'))
    else:
        return HttpResponseForbidden("Nemáš oprávnění k odstranění tohoto komentáře.")