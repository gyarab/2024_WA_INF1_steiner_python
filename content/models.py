from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Biom(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Biomes"

    def __str__(self):
        return self.name

#https://www.youtube.com/watch?v=GNsuF4xB80E&ab_channel=DaveGray

class Article(models.Model):
    title = models.CharField(max_length=200)
    zakladniInfo = models.TextField(default="Neznámé")
    dodatkovyText = models.TextField(default="Neznámé")
    vyroba = models.TextField(max_length=200, default="Neznámé")
    image = models.ImageField(default='default.jpg', blank=True)
    version = models.TextField(max_length=50, default="Neznámé")
    lastUpdate = models.DateTimeField()
    biom = models.ForeignKey(Biom, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category, related_name='articles')
    vote_sum = models.IntegerField(default=0)
    vote_count = models.IntegerField(default=0)
 
    def vote_avg(self):
        return self.vote_sum / self.vote_count if self.vote_count > 0 else 0      

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    time = models.DateTimeField(auto_now_add=True, null=True)
    ip = models.GenericIPAddressField(default=None, null=True)
    user_agent = models.CharField(max_length=200, default=None, null=True)

    def __str__(self):
        return f"{self.name} ({self.user.username if self.user else 'nepřiřazen'})"