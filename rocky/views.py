from django.shortcuts import render
from django.http import HttpResponse
from math import factorial

# Create your views here.

def index(request):
    return HttpResponse("<h1>welcome to views of myapp:rocky</h1>")

def home(request):
    return render(request,"rocky/htmlpage.html",{'message':"error 404 page not found"})

def fact(request,n):
    n=int(n)
    return HttpResponse("<h3>factorial of the number is {}</h4>".format(factorial(n)))

