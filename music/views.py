from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from . forms import MyRegFrm, LoginFrm
from django.contrib import messages
from django.http import HttpResponse
from .models import Music


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def myPlayer(request):
    if request.user.is_authenticated:
        music = Music.objects.all().order_by('title')
        music_list = list(Music.objects.all().order_by('title').values())
    # return HttpResponse(music_list, content_type='application/json')
        return render(request, 'home.html', {'musics': music, 'music_list': music_list})
    else:
        return redirect('/signin')

def regUser(request):
    if request.POST:
        form=MyRegFrm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your registration is successfull')
            except Exception as e:
                messages.error(request, e)
    else:
        form=MyRegFrm()
    return render(request, 'reg.html', {'form':form})

def loginUser(request):
    if request.POST:
        form=LoginFrm(request=request, data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/player')
    else:
        form=LoginFrm()
    return render(request, 'login.html', {'form':form})

def logoutUser(request):
    logout(request)
    return redirect('/signin')


