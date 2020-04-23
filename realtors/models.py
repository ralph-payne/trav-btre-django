from django.db import models
from datetime import datetime

# Create model Realtor & extend models.model
class Realtor(models.Model):
    # The id you don't have to start because it will be automatic
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True) # blank equals True makes it optional
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False) # Check off if they are seller of the month.
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    # Just like with listings, we need a main field; This field will be the Realtor's name
    def __str__(self):
        return self.name
