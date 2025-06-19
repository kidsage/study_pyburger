from django.http import HttpResponse
from django.shortcuts import render

def main(req):
    # return HttpResponse("Hi. It's pyburger")
    return render(req, "main.html")

def burger_list(req):
    # return HttpResponse("burger list")
    return render(req, "burger_list.html")
