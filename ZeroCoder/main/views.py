from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")

def data(request):
    return HttpResponse("<h1>С наступающим 2025 годом!</h1>")

def test(request):
    return HttpResponse("<h1>Благодарю Миру! Пусть 2025 год станет мирным во всём Мире!</h1>")
