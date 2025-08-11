from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Добро пожаловать на главную страницу!")

def data_page(request):
    return HttpResponse("Это страница данных. Здесь может быть ваша аналитика.")

def test_page(request):
    return HttpResponse("Тестовая страница! Проверка связи.")