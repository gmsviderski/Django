from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>Сайт посвящен фильму "Назад в будущее" </h1>')

def artists(request):
    return HttpResponse('<h1>Артисты, снимамающиеся в фильме </h1>')