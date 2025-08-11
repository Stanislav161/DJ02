from django.contrib import admin
from django.urls import include, path  # Добавьте include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Подключаем URL-адреса приложения
]
