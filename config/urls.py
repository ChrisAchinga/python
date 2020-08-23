from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('article.urls')),
    path('acount/', include('django.contrib.auth.urls')),
    path('acount/', include('account.urls')),
]
