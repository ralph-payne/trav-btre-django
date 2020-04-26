from django.shortcuts import render
from django.http import HttpResponse # Use this for troubleshooting if you want to see if the route is set up correctly

# Bring in search options (choices.py from the listings folder)
from listings.choices import bedroom_choices, price_choices, state_choices

# Bring in Listings model that will be used on the home page
from listings.models import Listing

# Bring in Realtors model that will be used on the about page
from realtors.models import Realtor

# Write function index
def index(request):
    # We use the same parameters as we did in listings/views.py but this time we also add [:3] to specify that we only want three listings
    latest_three_listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': latest_three_listings,
        # Pass in the dictionaries for the search bar
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
    }
    # Pass the context into the index template
    return render(request, 'pages/index.html', context)

# Write function/method about
def about(request):
    # Bring in all realtors from the database
    realtors = Realtor.objects.order_by('-hire_date')

    # Get mvp. Note, this allows for more than one mvp
    mvps = Realtor.objects.all().filter(is_mvp=True)
    
    context = {
        'realtors': realtors,
        'mvp_realtors': mvps
    }

    return render(request, 'pages/about.html', context)