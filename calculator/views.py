from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from . import connectDB
import redis
r = redis.StrictRedis(host="OnlineCalculatorRC.redis.cache.windows.net", port=6380, db=0, password="NzRTX7qXYe1ACTsi3nDYR3Ymkg3MZ2tRfAzCaMAaSXA=", ssl=True)

# Update connection string information 
db = connectDB.connection()
db.insert_data("add", 1, 1, 2)
db.insert_data("add", 2, 2, 4)
db.insert_data("add", 4, 4, 8)
db.insert_data("add", 8, 8, 16)
db.insert_data("add", 16, 16, 32)

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Brian's calculator")


def calc(request):
    num1 = request.POST.get('num1', 0)
    num2 = request.POST.get('num2', 0)
    req_str = str(num1) + "+" + str(num2)
    print(req_str)
    if req_str in r:
        res = int(r.get(req_str))
        print("[+] retrieving from cache")
        db.insert_data("add", num1, num2, res)
        print(res)
        return render(request, "input.html", {"result": res})

    res = int(num1) + int(num2)
    r.set(req_str, res)
    db.insert_data("add", int(num1), int(num2), res)
    print(res)
    return render(request, "input.html", {"result": res})

def hist_log(request):
    res = db.select_data()
    return render(request, "logs.html", {"result": res[0], "result2": res[1], "result3": res[2], "result4": res[3], "result5": res[4]})