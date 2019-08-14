from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices
# Create your views here.


def index(request):
    # order by date
    listings = Listing.objects.all().order_by('-listDate')[:3]
    context = {
        'list': listings,
        'title': "Home",
        "bedroom_choices":  bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    team = Realtor.objects.all()[:3]
    mvps = Realtor.objects.filter(is_mvp=True)
    context = {
        'mvps': mvps,
        'team': team
    }
    return render(request, 'pages/about.html', context)
