from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Home ')


def sobre(request):
    return HttpResponse('sobre')


def contatos(request):
    return HttpResponse('contatos')
