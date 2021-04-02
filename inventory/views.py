from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('<p>The index view</p>')

def item_detail(request, id):
	return HttpResponse('<p>The item_detail view to id {0}</p>'.format(id))

# Create your views here.


