from django.urls import path
# import views.py from the same folder. This file contains the methods you use below (index, listing, search)
from . import views

# If we leave the path empty '', it pertains to just /listings
urlpatterns = [
    # We want this to call the index method inside of the listings views file. We give it a name 'listings'
    path('', views.index, name='listings'),
    # We want the single listing to look something like /listings/23 (with 23 being the id)
    # Therefore, we need to include a parameter in our url. We do this by using angle brackets <> and the type (int) and then what we want to call it. That is how we will access our parameter from within the view method. The name of the method will be views.listing
    # <int:listing_id> is the way we will be able access the parameter from within the view method
    path('<int:listing_id>', views.listing, name='listing'),
    # Putting in search means that it will be listings/search. The reason we don't put listings/search here is because we are going to link this to the main urls.py and tell it that anything that has listings/ should look at this file
    path('search', views.search, name='search')
]
