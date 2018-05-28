from django.shortcuts import render
from .models import Cat
from .forms import CatForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

def index(request):
    cats = Cat.objects.all()
    form = CatForm()
    return render(request, 'index.html', {'cats':cats, 'form':form})

def show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'show.html', {'cat': cat})

def post_cat(request):
    form = CatForm(request.POST)
    if form.is_valid:
        cat = form.save(commit = False)
        cat.user = request.user
        cat.save()
    return HttpResponseRedirect('/')
    
def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cats': cats})
