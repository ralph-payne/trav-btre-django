from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

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
        
        # Check if user has already had an inquiry on this property
        if request.user.is_authenticated:
            # If the user is logged in, then grab their id from the request (this is a hidden input on the form)
            user_id = request.user.id
            # Create variable has_contacted and set it to our model Contact and objects.all()
            # all() is the method you use to retrieve all objects from a table (essentially you are querying the database here)
            # The filter listing_id=listing_id checks for the current listing and the current user
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            # The above variable will return truthy if the user with the user_id has already made an inquiry into this specific listing with ID listing_id
            if has_contacted:
                # If user has already made an enquiry, throw an error message
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)
        
        contact = Contact(user_id=user_id, listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message)

        contact.save()
        # We only want the email actually sent out if the contact has been saved
        send_mail(
            'Property Listing Inquiry' + listing, # Subject
            'There has been an inquiry for' + listing + 'Sign into the admin panel for more info', # Body of message
            'ralphpaynecode@gmail.com', # from@example.com (Here you use the EMAIL_HOST_USER you specified in settings.py)
            [realtor_email, 'ralphpayne@gmail.com'], # ['to@example.com'] List of email addresses
            fail_silently=True # This means it will show us some error messages if something goes wrong
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)