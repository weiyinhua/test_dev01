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

def index(request):
    """
    登录页面
    :param request:
    :return:
    """
    method = request.method
    if method=="GET":
        return render(request, "index.html")
    else:
        input_username = request.POST.get("username", "")
        input_password = request.POST.get("password", "")
        if input_username != "tom" or input_password != "123":
            # return HttpResponse("Error entering username or password")
            return render(request, "index.html", {"error": "Error entering username or password"})

        return HttpResponse("ok")
