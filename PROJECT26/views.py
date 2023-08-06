from django.shortcuts import render
from django.http import HttpResponse 

d={'vegetables':['tamotoes','beerkai','bottlefruite','kakarakai','onions','bendikai','gummadikai','carrots']}
d1={'a':10,'b':'50','c':'30'}
def hello(request):
    return HttpResponse("<h1>iam always talk to others with good expressed attitude</h1>")
def vegetables(request):
    return render(request,'vegetables.html',context=d)
def highest(request):
    return render(request,'highest.html',context=d1)
