import time

from django.shortcuts import render
from django.http import HttpResponse


def my_task():
    time.sleep(10)
    open('test.txt', 'w').close()


def home(request):
    my_task()
    return HttpResponse("Hello")
