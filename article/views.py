from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Article, News, ImageGallery
# from .forms import ContactForm

# Class Based Views
# Article Read
class ArticleView(DeleteView):
    model = Article
    template_name = 'article/article.html'

# News Read
class NewsView(DetailView):
    model = News
    template_name = 'article/news.html'

class CategoryView(DetailView):
    model = Category
    template_name = 'article/category.html'

# Forms
# Create Article
class CreateArticle(CreateView):
    model = Article
    template_name = 'article/add_article.html'
    fields = '__all__'

# Function Based Views
# Landing Page
def Landing(request):
    article = Article.objects.all()
    category = Category.objects.all()
    news = News.objects.all()
    context = {'article':article, 'category':category, 'news':news}
    return render(request, 'article/index.html', context)


# Forms
# contact us form
def contactView(request):
    context = {}
    return render(request, "article/contact.html", context)

