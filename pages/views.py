from django.shortcuts import render
from django.http import HttpResponse

# Write function index
def index(request):
    # render takes in two things: (i) the request itself and (ii) the location of the template
    return render(request, 'pages/index.html')

# Write function/method about
def about(request):
    return render(request, 'pages/about.html')