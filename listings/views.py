from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
# Create your views here.

def index(request):
    # get all data from listing database
    listings = Listing.objects.all()
    # pass database records into listings context. Make a dictionary
    context = {'listings': listings}
    return render(request, 'listings/listings.html', context) 
# the first listings is the app name. The second listings is the url name, define a dictionary with key = 'name', and value = 'something'.

def listing(request, listing_id):
    return render(request, 'listings/listing.html')
# Create your views here.

def search(request):
    return render(request, 'listings/search.html')
# Create your views here.