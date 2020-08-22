from django.urls import path
from . import views
from .views import ArticleView, NewsView, contactView, successView, CategoryView, CreateArticle

urlpatterns = [
    path('', views.Landing, name='home'),
    path('read/<int:pk>', ArticleView.as_view(), name='article'),
    path('news/<int:pk>', NewsView.as_view(), name='news'),
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
    path('category/<int:pk>/', CategoryView, name='category'),
    path('add_post/', CreateArticle.as_view(), name='add-post'),
]
