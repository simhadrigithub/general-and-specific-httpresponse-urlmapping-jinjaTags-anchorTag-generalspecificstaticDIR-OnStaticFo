from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
d={'fruits':['apples','grapes','mangos','fineapples','flowerfruite','orangefruite','guavefruite','kivifruite','watermelon','bananas']}
d1={'a':10,'b':20}
def nature(request):
    return HttpResponse("<marquee>i love beautiful nature</marquee>")
def simha(request):
    return HttpResponse("<h1>dont stop your working untill you get one soft job okk naa</h1>")
def fruits(request):
    return render(request,'fruits.html',context=d)
def bigvalue(request):
    return render(request,'bigvalue.html',context=d1)
