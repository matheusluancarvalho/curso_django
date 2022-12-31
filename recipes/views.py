from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('HOME 1')
    # return Http reponse


def contato(request):
    return HttpResponse('Contato')
    # return Http reponse


def sobre(request):
    return HttpResponse('Sobre')
    # return Http reponse
