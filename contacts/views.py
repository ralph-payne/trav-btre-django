from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Contact

def contact(request):

    # If it's equal to POST, we know that it's the inquiry form submission
    if request.method == 'POST':
        # As it is a POST Request, we want to capture the form fields. We get the form values from the name fields in templates/listings/listing.html
        # It doesn't matter if the field is a hidden field or a text field, we will capture them the same way
        user_id = request.POST['user_id']
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        # Note that the realtor_email is not included in the model
        realtor_email = request.POST['realtor_email']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        contact = Contact(user_id=user_id, listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message)

        contact.save()

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)