from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    name = request.GET.get("name",)
    return HttpResponse("Hello, " + name)