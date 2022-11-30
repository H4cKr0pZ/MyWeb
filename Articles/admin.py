from django.contrib import admin
from . models import Article , Gallery

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('Title','Description','Link')

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('Image','Caption')


# Register your models here.

admin.site.register(Article,ArticleAdmin)
admin.site.register(Gallery,GalleryAdmin)