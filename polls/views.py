from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "polls/list.html", {"ls": ls})


def home(response):
    return render(response, "polls/home.html", {})

