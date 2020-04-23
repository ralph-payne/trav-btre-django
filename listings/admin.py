from django.contrib import admin

# You know that you want to import Listing because that is the name you gave it in listings/models.py
from .models import Listing

# Register model
# def register(self, model_or_iterable, admin_class=None, **options):
admin.site.register(Listing)
