from django.shortcuts import render, get_object_or_404
from .models import *

def home(request):
	return render(request, 'app/home.html')


def our_story(request):
	return render(request, 'app/our_story.html')


def community(request):
	return render(request, 'app/community.html')


def menu_list(request):
	menus = Menu.objects.all()
	return render(request, 'app/menu_list.html', {'menus':menus})


def newsevent_list(request):
	news = NewsEvent.objects.all()
	return render(request, 'app/newsevent_list.html', {'news':news})