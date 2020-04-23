from django.shortcuts import render
from django.http import HttpResponse # Use this for troubleshooting if you want to see if the route is set up correctly

# Write function index
def index(request):
    # render takes in two things: (i) the request itself and (ii) the location of the template
    return render(request, 'pages/index.html')

# Write function/method about
def about(request):
    return render(request, 'pages/about.html')