from email.mime import image

from .models import level, photo
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request) :
    obj=level.objects.all()
    print(obj)
    return render(request, "index.html",{'result': obj})
def img(request) :
    obj1 = photo.objects.all()
    print(obj1)
    return render(request, "index.html", {'result1': obj1})
