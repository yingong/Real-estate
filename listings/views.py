from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .choices import bedroom_choices, price_choices, state_choices
# Create your views here.


def listings(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'list': paged_listings,
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = (Listing.objects.filter(id=listing_id))[0]
    context = {
        'list': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    if not len(request.GET):
        listings = Listing.objects.all()
    else:
        if 'keywords' in request.GET:
            listings = Listing.objects.filter(
                description__icontains=request.GET['keywords'])
        if 'city' in request.GET and request.GET['city']:
            listings = listings.filter(city__iexact=request.GET['city'])
        if 'state' in request.GET and request.GET['state']:
            listings = listings.filter(state__iexact=request.GET['state'])
        if 'bedrooms' in request.GET and request.GET['bedrooms']:
            listings = listings.filter(
                bedrooms__iexact=request.GET['bedrooms'])
        if 'price' in request.GET and request.GET['price']:
            listings = listings.filter(price__lte=request.GET['price'])
    listings = listings.order_by('-listDate')
    context = {
        "bedroom_choices":  bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
        "listings": listings,
        "values": request.GET
    }
    return render(request, 'listings/search.html', context)
