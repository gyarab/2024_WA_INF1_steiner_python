from django.db import models

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

    def __str__(self):
        return self.title



