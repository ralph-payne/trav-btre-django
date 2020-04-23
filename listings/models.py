from django.db import models
from datetime import datetime
# Bring in the Realtor model from the realtor app
from realtors.models import Realtor

# The way we define a model is with the keyword Class. It should be the singular version of the app. This app is called listings, so the model should be called Listing
# models.Model is extending the core model, which gives us a lot of stuff to work with
class Listing(models.Model):
    # Create properties
    # The realtor one is the most difficult one to create as it is part of another table. We need to use the expression 'foreign key' so that we can form a relationship between realtors and listings
    # ForeignKey takes in two parameters. (i) the name of the other model that we are relating (ii) what to do when you delete (in this case, if you have a realtor related to a listing, and you delete the listing, what do you want to happen to the listing? Do you want the listing to delete too? In this case, we do not want the listing to delete so we state DO_NOTHING
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True) # a text field is different because it is a little longer
    price = models.IntegerField() # not a float because we're not going to do decimal points on prices of homes
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1) # We actually want this to be a decimal not an integer
    garage = models.IntegerField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1) # For example, 1.2 acres
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/') # we're not actually storing images in a database; wer're storing the location of the image. That way we can fetch the location and can simply put it into an img src so that it displays on the page
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # photos 1-6 are optional so we include blank=True
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True) # So that the client can publish & unpublish listings
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    # We need to pick a field that will be the main field to be displayed. It probably makes sense for that field to be the title in this case. 
    def __str__(self):
        return self.title