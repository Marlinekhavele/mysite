from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "polls/list.html", {"ls": ls})


def home(response):
    return render(response, "polls/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, "polls/create.html", {"form": form})

