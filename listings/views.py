from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'listings/listings.html', {'name':'something'}) 
# the first listings is the app name. The second listings is the url name, define a dictionary with key = 'name', and value = 'something'.

def listing(request):
    return render(request, 'listings/listing.html')
# Create your views here.

def search(request):
    return render(request, 'listings/search.html')
# Create your views here.