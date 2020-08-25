from django.urls import path
from . import views
from .views import ArticleView, NewsView, CategoryView, CreateArticle, loginForm, registerForm, Magazine, CreateNews

urlpatterns = [
    path('', views.Landing, name='home'),
    path('read/<int:pk>', ArticleView.as_view(), name='article'),
    path('news/<int:pk>', NewsView.as_view(), name='news'),
    path('category/',views.CategoryView, name='category'),
    path('add_article/', CreateArticle.as_view(), name='add-article'),
    path('add_news/', CreateNews.as_view(), name='add-news'),
    path('magazine/', views.Magazine, name='magazine'),
    path('accounts/register', views.registerForm, name='register'),
    path('accounts/login', views.loginForm, name='login'),
    path('accounts/logout/', views.logoutUser, name="logout"),
]
