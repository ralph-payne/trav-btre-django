# We have three view methods (in listings/urls.py) that we want to create
from django.shortcuts import render
from django.http import HttpResponse # Use this for troubleshooting if you want to see if the route is set up correctly

# Bring in the paginator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Bring in our model
from .models import Listing

def index(request):
    # Create variable called listings and set it to the model name called Listing. This variable will get passed into the dictionary 'context'
    # We add a order_by and a filter as well
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # Include paginator & pass in listings (variable above from the database) & the number of listings we want per page
    paginator = Paginator(listings, 6) # Show 6 listings per page
    # Create variable called page from the get request; when the user is on page 2, there will be a url paramater that will say page=2
    page_number = request.GET.get('page')
    # Pass the page into Paginator
    paged_listings = paginator.get_page(page_number)

    # Create variable that we will pass into the render function
    context = {
        # The key is 'listings'; the value is the variable you created above (all the objects from the model Listing)
        # A common mistake here is to write 'listing' instead of 'listings' or the other way round. A lot of the typos are because you have written singular when it should be plural or you have writting plural when it should be singular
        'listings': paged_listings
    }

    # Pass the context into the template
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    # render takes in two things: (i) the request itself and (ii) the location of the template
    return render(request, 'listings/search.html')