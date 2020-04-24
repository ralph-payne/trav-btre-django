from django.contrib import admin

# You know that you want to import Listing because that is the name you gave it in listings/models.py
from .models import Listing

# Create class so we can edit tables in admin view & pass in admin.ModelAdmin as a parameter
# We also need to pass it into the model we registered at the bottom of the page
class ListingAdmin(admin.ModelAdmin):
    # Define what we want in the table/list, i.e. we have to ask ourselves "What do we want to see here?"
    # Whenever you do a boolean value (like is_published), Django will show a checkbox or an 'x'
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    # list_display_links changes what you can click on to take you to a listing
    list_display_links = ('id', 'title')
    # Include functionality to filter by realtor (note that as there's only one value, we need to include a comma after)
    list_filter = ('realtor', )
    # Include functionality that allows us to publish or unpublish simply by clicking on the checkbox
    list_editable = ('is_published', )
    # Include functionality that allows us to search by certain fields
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    # Include pagination
    list_per_page = 25

# Register model
# def register(self, model_or_iterable, admin_class=None, **options):
admin.site.register(Listing, ListingAdmin)

