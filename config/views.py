from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger

def main(req):
    # return HttpResponse("Hi. It's pyburger")
    return render(req, "main.html")

def burger_list(req):
    # return HttpResponse("burger list")
    burgers = Burger.objects.all()
    print(burgers)

    context = {
        "burgers": burgers
    }
    return render(req, "burger_list.html", context)

def burger_search(req):
    # print(req.GET)
    keyword = req.GET.get("keyword")
    # print(keyword)

    burgers = Burger.objects.filter(name__contains=keyword)
    context = {
        "burgers": burgers
    }
    return render(req, "burger_search.html", context)