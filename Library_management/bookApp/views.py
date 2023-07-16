from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Author


# Create your views here.


def list_authors(request):
    authors = Author.objects.all()


def welcome(request):
    return HttpResponse('Obele welcome')
