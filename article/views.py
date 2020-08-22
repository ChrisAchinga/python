from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Article, News, ImageGallery
from .forms import ContactForm

# Function Based Views
# Landing Page
def Landing(request):
    article = Article.objects.all()
    category = Category.objects.all()
    news = News.objects.all()
    context = {'article':article, 'category':category, 'news':news}
    return render(request, 'article/index.html', context)

# contact us form
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "article/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

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

class CreateArticle(CreateView):
    model = Article
    template_name = 'article/add_post.html'
    fields = '__all__'
 
# functional views
