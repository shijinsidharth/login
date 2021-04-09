from django.shortcuts import render
from django.http import HttpResponse
def Testfn(request):
    return HttpResponse('hlooooo')
def html1(request):
    return render(request,'login.html')
# Create your views here.
