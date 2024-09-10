from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choices import price_choices, bedroom_choices, district_choices
# Create your views here.

def index(request):
    # get all data from listing database
    #listing_id = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)

    #GET is html method while get is a function.
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    # pass database records into listings context. Make a dictionary
    context = {'listings': paged_listings}
    return render(request, 'listings/listings.html', context) 
# the first listings is the app name. The second listings is the url name, define a dictionary with key = 'name', and value = 'something'.

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context ={'listing': listing}
    return render(request, 'listings/listing.html', context)
# Create your views here.

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET: # check if existence of key words in search
        keywords = request.GET['keywords'] #if words entered, put such words into "keywords"
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords #icontains means case insensitive
            )
    if 'title' in request.GET: # check if existence of key words in search
        title = request.GET['title'] #if words entered, put such words into "keywords"
        if title:
            queryset_list = queryset_list.filter(
                title__icontains=title 
            )
    if 'District' in request.GET: # check if existence of key words in search
        District = request.GET['District'] #if words entered, put such words into "keywords"
        if District:
            queryset_list = queryset_list.filter(
                district__iexact=District #means exact
            )
    if 'price' in request.GET: # check if existence of key words in search
        price = request.GET['price'] #if words entered, put such words into "keywords"
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price #lte mean less than and equal
            )
    if 'bedrooms' in request.GET: # check if existence of key words in search
        bedrooms = request.GET['bedrooms'] #if words entered, put such words into "keywords"
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms #lte mean less than equal
            )

    context = {
        'district_choices': district_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_list

    }
    return render(request, 'listings/search.html', context)
# Create your views here.