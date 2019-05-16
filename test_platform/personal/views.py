from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    """
    :param request:
    :return:
    """

    input_name = request.GET.get("name","")#获取（get）,GET请求(http://127.0.0.1:8000/hello/?name=tom1)
    if input_name=="":
        return HttpResponse("Please input 'http://127.0.0.1:8000/hello/?name=name1'")

    #return HttpResponse("Hello, " + name)

    return render(request, "index.html",{"get_name":input_name})