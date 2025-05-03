from django.urls import path
from .views import articles, article, category
from . import views
from django.urls import include

app_name = 'content'

urlpatterns = [
    path('', articles, name='articles'),
    path('article/<int:id>/', article, name='article'),
    path('rubrika/<int:id>/', category, name='category'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('oauth/', include('social_django.urls', namespace='social')),
]

