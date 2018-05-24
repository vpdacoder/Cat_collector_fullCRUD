from django.shortcuts import render
from .models import Cat

def index(request):
    cats = Cat.objects.all()
    return render(request, 'index.html', { 'cats':cats })
