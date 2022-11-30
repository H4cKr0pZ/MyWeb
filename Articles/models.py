from django.db import models

# Create your models here.

class Article(models.Model):
    Title = models.CharField(max_length=255)
    Description = models.CharField(max_length=3000)
    image = models.CharField(max_length=3000)
    Link = models.CharField(max_length=2500)


class Gallery(models.Model):
    Image = models.CharField(max_length=3000)
    Caption = models.CharField(max_length=300)
    Link = models.CharField(max_length=2500)