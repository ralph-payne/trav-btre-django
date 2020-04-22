# We have three view methods (in listings/urls.py) that we want to create
from django.shortcuts import render

# Write function index. index will be the main listings page
def index(request):
    # render takes in two things: (i) the request itself and (ii) the location of the template
    return render(request, 'listings/listings.html')

# Write function listing
def listing(request):
    return render(request, 'listings/listing.html')

# Write function search
def search(request):
    return render(request, 'listings/search.html')