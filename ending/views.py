from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Ending index.")

def find(request):
    return HttpResponse("Here you can find the ending of you serie/anime")