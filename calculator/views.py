from django.shortcuts import render
from django.http import HttpResponse
res = 0
# Create your views here.
def index(request):
    return HttpResponse("Welcome to Brian's calculator")


def calc(request):

    num1 = request.POST.get('num1', 43)
    num2 = request.POST.get('num2', 26)

    res = num1 + num2
    return render(request, "input.html", {"result": res})

def add(request):
    return render(request, "result.html", {"result": res})

def hist_log(request):
    return HttpResponse("logs")