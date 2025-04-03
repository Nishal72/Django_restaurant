from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Item
# Create your views here.

def home(request):
    Items=Item.objects.all()
    return render(request, 'menu/home.html', {'items':Items})

def about(request):
    return HttpResponse("This is the about page.It contains the about.")