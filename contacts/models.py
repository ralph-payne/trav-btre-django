from django.db import models
from datetime import datetime

# Models are always singular and always have a uppercase first letter
class Contact(models.Model):
    # Listings will be a charfield
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    # This will be the contact name
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    # Message field will be optional, so we include blank=True
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    # User ID will be connected to whatever registered user is logged in when they make an inquiry
    # We set it as optional (blank=True) as when someone makes an inquiry, they may not be logged in.
    # You don't want inquiry forms available to only those who are logged in, but if they are logged in, you are going to want to track their ID
    user_id =  models.IntegerField(blank=True)

    # Define main field that we want to refer to for this model
    def __str__(self):
        return self.name