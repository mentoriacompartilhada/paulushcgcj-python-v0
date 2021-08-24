"""Define the content of the views"""
from django.http import HttpResponse


def hello(request):
    """Define a hello view that prints hello world"""
    return HttpResponse("Hello World")
