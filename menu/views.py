from django.http import HttpResponse
from django.shortcuts import render
from menu.models import Item

# Create your views here.

def home(request):
    
    items = Item.objects.all()
    return render(request, 'menu/home.html', {'items': items})

def about(request):
    return HttpResponse("This is the about page.")
