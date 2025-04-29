from django.urls import path
from .views import articles, article, category
from . import views

app_name = 'content'

urlpatterns = [
    path('', articles, name='articles'),
    path('article/<int:id>/', article, name='article'),
    path('rubrika/<int:id>/', category, name='category'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
