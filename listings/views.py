# We have three view methods (in listings/urls.py) that we want to create
from django.shortcuts import render
from django.http import HttpResponse # Use this for troubleshooting if you want to see if the route is set up correctly

# Write function index. index will be the main listings page
def index(request):
    # render takes in two things: (i) the request itself and (ii) the location of the template
    return render(request, 'listings/listings.html')
    # return HttpResponse('<h1>Success1 with HttpResponse</h1>')

def listing(request):
    return HttpResponse('<h1>Success individual listing</h1>')
    # return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')