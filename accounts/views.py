from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from contacts.models import Contact

# When the requests get submitted, we need to identify if we are seeing a GET or POST request

def login(request):
    # If it's equal to POST, we know that it's the form submission
    if request.method == 'POST':
        # Get form values using POST and the input name. We get the form values from the name fields in templates/accounts/login.html
        username = request.POST['username']
        password = request.POST['password']

        # To be able to login or authenticate, we want to create a variable called user and use the authenticate method
        # You need to bring it in from django.contrib.auth
        user = authenticate(username=username, password=password)

        if user is not None:
            # If user is not None, this means that the user is found. auth.login takes in the request and the user
            # https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.login
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            # If the user is not found, return an error
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        # If it's not a POST Request, it's a GET Request, so render the page
        return render(request, 'accounts/login.html')

def logout(request):
    # Check if it is POST Request
    if request.method == 'POST':
        # If it is a POST Request, we want to logout. This has one parameter
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def register(request):
    if request.method == 'POST':
        # Get form values using POST and the input name (in this case first_name). We get the form values from the name fields in templates/register.html
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Do validation to check if passwords match
        if password == password2:
            # If they do match, we move on but we have more validation to do. We don't want duplicate emails and we don't want duplicate usernames
            # To check username, we need to bring in the username model (which comes as a default with Django) from django.contrib.auth.models import User
            # The objects method fetches from the database. We want to put a filter by username=username, which means that we are checking the username field in the database for this value in the variable we declared above
            # Add .exists method(). This method lets us know if that username exists
            if User.objects.filter(username=username).exists():
                # If true, show an error
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                # Another check for the email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good, so you can now create the user in the database
                    # Create variable called user & use the Django helper function create_user
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

                    # Option 1: Login after register, which passes in the request and the user you just created. You need to bring it (auth) in; it is part of django.contrib
                    # auth.login(request, user)
                    # Add message
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')

                    # Option 2: Redirect user to login page
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            # Redirect to same page
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

    
def dashboard(request):
        
    # Check to see if user is logged in (same logic as contacts/views.py)
    if request.user.is_authenticated:
        # If the user is logged in, then grab their id from the request (this is an hidden input on the form)
        user_id = request.user.id

        # Retrieve all contacts (to do this you need to bring in the Contact model)
        user_contacts = Contact.objects.all().order_by('-contact_date').filter(user_id=user_id)

        # Pass contacts into a context dictionary
        context = {
            'contacts': user_contacts
        }         

        # Return dashboard and pass in the context
        return render(request, 'accounts/dashboard.html', context)
    
    else:
        return redirect('register')