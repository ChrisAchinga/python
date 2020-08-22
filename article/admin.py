from django.contrib import admin
from .models import Article, News, Category, ImageGallery

# page titles
admin.site.site_header = 'Coast Woman'
admin.site.site_title = 'Coast Woman'
admin.site.index_title = 'Coast Woman Admin'

# Models Registration
admin.site.register(Article)
admin.site.register(News)
admin.site.register(Category)
admin.site.register(ImageGallery)