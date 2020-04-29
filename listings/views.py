# We have three view methods (in listings/urls.py) that we want to create: (1) index (2) listing (3) search
# Bring in render as standard and get_object_or_404 for individual listing
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse # Use this for troubleshooting if you want to see if the route is set up correctly

# Bring in search options (choices.py from the listings folder)
from .choices import bedroom_choices, price_choices, state_choices

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

    # Instead of Listings.objects, we use get_object_or_404(), which calls get() on a given model manager, but raises Http404 instead of the model's DoesNotExist exception
    # If you do not do this, the app could crash if a user searched for a listing in the url paramater that did not exist
    # https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/
    # You pass in two things (1) is the model (2) is the primary key (pk)
    # In listings/urls.py, you can see that the listing_id is passed through the url => path('<int:listing_id>', views.listing, name='listing')
    # You also need to bring in get_object_or_404 at the top (it's from django shortcuts)

    one_listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'one_listing': one_listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    
    # Create QuerySet list which we can build onto
    # class QuerySet(model=None, query=None, using=None, hints=None)
    # https://docs.djangoproject.com/en/3.0/ref/models/querysets/
    queryset_list  = Listing.objects.order_by('-list_date')

    # Comment all the fields
    # Keywords
    # Check if it exists by  
    # When you make a request with this form, it is a get request and you can actually test to see if it exists
    if 'keywords' in request.GET:
        # If it exists, we create a variable & we get the actual form value
        # Note that you need square brackets
        keywords = request.GET['keywords']
        # We then do another if to check that it is not an empty string
        if keywords:
            # Set a filter on our query_set_list and we search the description for any keywords that are typed into the keywords box
            # We are doing a search that is not an exact match (i.e. we're not looking for alabama = alabama, we're looking for one word inside a block of text)
            # Therefore, we need to use icontains (icontains is a case-insensitive containment test)
            # To test, find a word in one of the property descriptions and perform a search on it
            # Once you've tested successfully, you also are going to need to change <form action="search.html"> to <form action="{% url 'search' %}">
            # Note that if you now search for nothing, you will get all the listings
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # 'city' is also a text field, but with city we want to match the exact text string (i.e. we're looking for chicago & we want the exact match. not like when you search for 'pool' in the description field
    # City
    if 'city' in request.GET:
        # Create a variable called city
        city = request.GET['city']
        # Check that city is not an empty string
        if city:
            # The difference here is that you want an exact match instead of just contains. Ergo, you should use iexact instead of icontains. iexact is a case-insensitive exact match
            # If you wanted to make it case sensitive, then you should use 'exact' instead of 'iexact'
            # https://docs.djangoproject.com/en/3.0/ref/models/querysets/
            # You should now test the localhost:8000 by performing a query for city
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': queryset_list,
        # Add 'values' as a key and the whole get request is the value. That will mean that the whole get request will be available for us to use in the html template
        # As an example, if we search for search?keywords=pool&city= then request.get.keywords will be available to us as values.keywords
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)