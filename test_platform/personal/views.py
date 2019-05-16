from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    name = request.GET.get("name1","")#获取（get）,GET请求(http://127.0.0.1:8000/hello/?name1=tom1)
    return HttpResponse("Hello, " + name)