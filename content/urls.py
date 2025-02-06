from django.urls import path
from .views import articles, article, category

app_name = 'content'

urlpatterns = [
    path('', articles, name='articles'),
    path('article/<int:id>/', article, name='article'),
    path('rubrika/<int:id>/', category, name='category'),
]
