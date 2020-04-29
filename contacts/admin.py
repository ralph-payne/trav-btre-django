from django.contrib import admin

# Import Contact model from the models.py file in the same directory
from .models import Contact

# Create ContactAdmin class
class ContactAdmin(admin.ModelAdmin):
    # Define what you want to see in the table (i.e. make customizations)
    # It's helpful to go into contacts/models.py and have a look at the Model
    # https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    # Which ones do we actually want to be links
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

# Register model: def register(self, model_or_iterable, admin_class=None, **options):
admin.site.register(Contact, ContactAdmin)