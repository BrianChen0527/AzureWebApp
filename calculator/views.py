from django.shortcuts import render
from django.http import HttpResponse
from . import connectDB
# Update connection string information 
res = 0
db = connectDB.connection()
db.insert_data("add",1,2,3)
db.insert_data("add",1,2,3)
db.insert_data("add",1,2,3)
db.insert_data("add",1,5,6)
db.insert_data("add",1,0,1)
db.insert_data("add",1,2,3)
# Create your views here.
def index(request):
    return HttpResponse("Welcome to Brian's calculator")

def calc(request):
    num1 = int(request.POST.get('num1', 0))
    num2 = int(request.POST.get('num2', 0))
    res = num1 + num2
    db.insert_data("added", num1, num2, res)
    return render(request, "input.html", {"result": res})

def hist_log(request):
    res = db.select_data()
    return render(request, "logs.html", {"result": res[0], "result2": res[1], "result3": res[2], "result4": res[3], "result5": res[4]})