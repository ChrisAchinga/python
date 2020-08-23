from django.urls import path
from . import views
from .views import ArticleView, NewsView, CategoryView, CreateArticle, loginForm, registerForm

urlpatterns = [
    path('', views.Landing, name='home'),
    path('read/<int:pk>', ArticleView.as_view(), name='article'),
    path('news/<int:pk>', NewsView.as_view(), name='news'),
    path('category/<int:pk>/', CategoryView, name='category'),
    path('add_article/', CreateArticle.as_view(), name='add-article'),
    path('accounts/register', views.registerForm, name='register'),
    path('accounts/login', views.loginForm, name='login'),
    path('accounts/logout/', views.logoutUser, name="logout"),
]
