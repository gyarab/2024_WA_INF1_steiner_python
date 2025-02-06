from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    perex = models.TextField()
    text = models.TextField()
    published = models.DateTimeField()
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category, related_name='articles')

    def __str__(self):
        return self.title



