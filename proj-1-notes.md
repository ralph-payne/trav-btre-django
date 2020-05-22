*Note to self: Find out best way of hiding passwords, i.e. what is the Django equivalent of a dot env file?*
*Note to self: A data breach on your site exposed your password. Chrome recommends changing your password* => You normally get this error if you give the password as the same as the username

*Note to self: Work out best practices for different headers*
*Note to self: Work out best practices for notes to self*
*Note to self: best practice for questions/doubts?*

source ./venv/Scripts/activate && pip freeze && python manage.py runserver
$ source ./venv/Scripts/activate && pip freeze && python manage.py runserver

**Note to self - clean up these notes at the beginning**
**Note to self - see what happens when you put these notes into Google Docs**
**Note to self - disable the touch pad on your laptop**
**Note to self - remove the static files from git**
**Note to self - have a look at this https://www.toptal.com/designers/htmlarrows/**

#Notes to transfer to different cribs

`Bootstrap`
**Bootstrap CDN or locally?**
There are many good reasons to use a CDN in a Production environment
1. It increases the parallelism avaiable
2. It increases the chance that there will be a cache-hit
3. It ensures that the payload will be as small as possible
4. It reduces the amount of bandwidth used by your server
5. It ensures that the user will get a geographically close response

Stack Overflow recommends that you include the CDN and then the local file as a fallback

`Git Deployment`
git reset will unstage all the files you added after your last commit. This is useful for when you accidentally called git add -A and want to undo that action
Brad has his SSL keys set up for github - what does this mean?

```bash
Check what you have inside .gitignore
cat .gitignore
```

`Google Chrome`
Create a crib for Chrome
There are some absolutely fantastic 
https://support.google.com/chrome/answer/157179?hl=en
Ctrl + l => Jump to the address bar
Ctrl + k => Search from anywhere in the page (i.e. you start a new search in DuckDuckGo within your the same tab you are in)
Down Arrow + Shift + Delete => Remove predictions from your address bar
Ctrl + f + [text you want] + [Enter until you find it] + Esc => Jump to a specific place on the page
Alt + Left Arrow => Previous page in history
Alt + Right Arrow => Next page in history
Ctrl + Enter => Open link on new tab

`Google Sheets`
https://support.google.com/docs/answer/181110?co=GENIE.Platform%3DDesktop&hl=en
Alt + i + w + b => Insert row below `this is not a good one because there is another keyboard shortcut for drawing that could potentially mess it up. better to use insert row above`
Alt + i + r => Insert row above
Shift + Space => Select Row / deselect row `useful for deleting`
Ctrl + Space => Select Column / Deselect Column 
Ctrl + Alt + - => Delete Row (helps if you select the row first)

`HTML entities`
https://www.toptal.com/designers/htmlarrows/


====**NOTES ON TRAVERSY DJANGO BTRE PROJECT START HERE**===

**The Application Explained**
Front End:
- We are using PostgreS for a database
- We have Realtors - A person or business that sells or leases out real estate. These are pulled from the database
- We have six per page and then we use pagination logic
- Realtors and listings will have a relationship so that we can always click on realtor to see all their listings
- We will use Litebox 2 for the images
- We have a model for the 'make an enquiry form' 
- The search is simple but it shows you how to build query sets and how to filter your data when you're fetching from the database
- We use Django messages for alerts and stuff. We format them with Bootstrap. We add a little bit of JavaScript as well
- We have log in and sign up

Back Office:
- There is a relationship between the realtor and the listings
- We can upload images
- We have "seller of the month". Is MVP

**Bootstrap Theme**
At lot of times on a team, you will handed a HTML/CSS theme, and as the backend developer you'll turn it into a real application. 
The Bootstrap Theme is kept in the dist folder
Traversy used Sass because he wanted to customize the Bootstrap colors
Traversy edited the variables to match the branding colors
The partials (the underscores) don't get compiled. 
The only files that can compiled into regular CSS is `style` and `bootstrap`
Inside the CSS folder, you will see the compiled style.css file and the bootstrap.css (custom bootstrap css file with custom colors)
all.css is font awesome. Traversy is including everything locally; he's not including an CDNs (Content Delivery Networks) or anything like that.
Including Bootstrap locally means that if there is a later version of Bootstrap out, you won't need to change classNames
Traversy highly recommends using the local files rather than the CDNs so that you don't get caught up with potential issues for later versions of Bootstrap
Traversy also included jquery locally
The best way to look at the theme is to open it with Live Server in Visual Studio Code
We have a inquiry modal (the form for users to make a request)

**Lightbox**
We have a lightbox.min.css and lightbox.min.js
This is from Lightbox 2; it's great for doing sets of images in case you want to scroll through some images

**Show packages and dependencies installed on Global Scope**
$ pip3 freeze
Shows the packages and dependencies that are installed on a global scope on our system

**Create Virtual Environment**
The first thing we need to do is create a virtual environment in Python; this is necessary to keep all your packages and dependencies isolated inside of your project rather than in a global scope. 
You can use the venv package, which is included in Python, to create your environment.

$ python --version `check which version of python you are running. You want it to be python 3+`
$ python -m venv ./venv `Here you are saying that you want a folder called venv inside the current project directory`

This means that we have created the environment but we are not actually in it. You can test this by running $ pip freeze which will show you everything you have already installed globally.

**Activate the Environment**
The way you activate the environment depends on whether you are on a Mac or Windows. To activate the environment on Windows
$ ./venv/scripts/activate.bat
This should run your virtual environment if you are on Windows

There seems to be a bug here. The above code doesn't work so you should follow this solution instead:
*I seemed solve this by using what Brad describes as the mac method for activating the environment even though I'm in windows.  I had to do* 
"source ./venv/Scripts/activate" instead of just "./venv/Scripts/activate.bat"
$ source ./venv/Scripts/activate

**Issues with Python**
If you have issues, you may have to add this to the settings.json
```json settings.json
{
    "python.pythonPath": "C:\\Users\\Ralph\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"
}
```

**Issues with Pip**
If you get an error such as "Fatal error in launcher: Unable to create process using '"c:\users\ralph\cribs\python\proj-1\venv\scripts\python.exe"  "C:\Users\Ralph\cribs\1-py-trav-btre\venv\Scripts\pip.exe" install django'"
you should install pip
$ python -m pip

Alternatively, try upgrading pip
$ python -m pip install --upgrade pip

**Test that you are in the environment**
To test you should run
$ pip freeze `You want to see (venv)`

**Django Install**
Make sure you are inside of your environment
$ pip freeze
Then install django inside of your environment
$ pip install django

This will not be installed globally. To check that you have installed it in your environment, you should run
$ pip freeze `This should return a list of programs that have been installed to your environment`

**Create Django Project**
To create a Django Project, you want to use a CLI program called django-admin
$ django-admin help

Django has a project entity (which is your main project) and it also has apps. You have one project which is your main application and then inside that you have apps.

$ django-admin startproject btre .

This created a btre folder with some files; it also created a manage.py. You never touch manage.py. It is the tool we will now use instead of django-admin

You can have a look here; this shows you that you have a lot of the same commands a Django admin has only manage.py is more localised to this project
$ python manage.py help

**DRF**
https://www.fullstackpython.com/django-rest-framework-drf.html
DRF = Django REST Framework


**manage.py**
We we always use manage.py when doing migrations, run python server, create super use

**Linter**
You may have issues if you are using the linter
You could get import errors because the linter thinks that Django is not installed because the linter is looking at your global environment
To fix this in Visual Studio Code, you can open your command palette (Ctrl + Shft + P), and search for Python: Select Interpreter
You then want to choose the interpreter as your virtual environment

You can then install the linter

**git init**
git ignore
You should go to gitignore.io and it will give you a default gitignore file

You should include your venv

The way to do git Traversy was is:
$ git init
$ git add . && git commit -m 'Initial commit'

**Run dev server in Django**
You use the dev server to develop locally
When we run the server, it will create a couple of files
$ python manage.py runserver

If this doesn't work, you might not be in the right environment
$ pip freeze
$ source ./venv/Scripts/activate `do this if pip freeze tells you're not in the local environment`
$ pip freeze `check that you are now in the local environment`
$ python manage.py runserver `run server on port 8000`

The warning sign 'You have 17 unapplied migration(s)...' just means that some of the default apps that come with Django (e.g. auth and admin area) haven't been applied yet. You can ignore this message

**Opening up other tabs for terminals**
When you run the server, you are also going to want to open up another tab to run commands. You can switch back and forth with the termainl tabs

**localhost:8000**
Once you have your dev server running, you can open Chrome and have a look at localhost:8000. You should see the landing page for Django

**Exploring the initial files**
db.sqlite3 file is created when you run the server. This is where your data will be stored if you use the SQLite database. We won't use this because SQLite is not great for a real production application. SQLite is nice for prototyping and testing and if you have a small website with very little data and traffic.

**__pycache__ folder**
The __pycache__ folder will be generated when you run the server; you won't have to touch these at all. It just means that your program will start a little faster. Even if you delete this folder, it will run again when you start your server again.

**settings.py**
The settings file is the most important one we have. It has a lot of key-value pairs.
BASE_DIR is the project's main directory
The SECRET_KEY is for production. It's very important to remember that when you deploy a Django website, you never want to secret_key to be shared. You want to keep it secret by hiding it.

Inside settings.py DEBUG is set to `True`. In dev, you want to keep it as `True` but in production you will want to change it to `False`. It gives us helpful messages when things go wrong. It displays info about our code in the browser. In Production, even if something goes wrong, you don't want that information displayed in the browser because then anybody will be able to see it & therefore it represents a security risk.

ALLOWED_HOSTS = []
This is an empty array at first, but when we deploy you want to put a list of host domains that this website can serve. For instance, the Digital Ocean IP address or any domain names

Django has a concept of apps; you can have multiple apps per project. For example, in our project we will have a listings app, a realtors app etc. Django includes some default apps

Templates are what are used to generate HTML for our application to display to the user.

Databases is where you want to set up your database paramenters. The default is SQLite but we will change it to PostgreSQL. 

STATIC_URL is the path we want to use for static files (CSS etc)

**urls.py**
urls.py is basically our routing file
We have a urlpatterns list.
We put in paths (with a forward slash at the end)
You can link the paths to a view method or you can link to the urls from another file (in this case admin urls)

Every app that we create (e.g. our listings app), it will create a new folder called listings and we will create a new urls.py in the listings app & then we will bring that into the main urls.py

**wsgi.py**
WSGI stands for Web Server Gateway Interface. It's a specification that describes how a web server communicates with web applications & how web applications can be chained together to process one request.

=====
**URLs and Views (urls.py and views.py)**
To understand urls.py and views.py in Django, you should picture a triange with (i) the browser (ii) urls.py (iii) views.py
Imagine we are in a browser and we make a request to the /about url. We expect to see an about page returned to us in the browser
The job of urls.py is to look at the request url and then decide which function to fire in our Django code within the views.py file
An example
(1) The user goes to /about
(2) The urls.py file looks at the url and says "I want to find a function inside views.py called 'about'. The function can be called whatever you want but it probably makes sense to call it something logical like 'about'
(3) Inside the function within views.py we can control what happens when the user visits the url. Ideally we will send back a response to the browser 

**startapp**
https://docs.djangoproject.com/en/3.0/ref/django-admin/
`startapp` creates a Django app directory structure for the given app name in the current directory or the given destination. By default, the new directory contains a models.py file and other app template files. If only the app name is given, the app directory will be created in the current working directory.
django-admin startapp name [directory]

**Creating Apps in Django**
You have multiple apps per project. We are going to create the pages app which will take care of displaying the home page and the about page and any other static pages that you want to create. To create an app, first of all you should check that you are in the right environment (pip freeze). Then type this:
$ python manage.py startapp pages `where pages is the name of the app you want to create`

That then creates a new folder called pages. Within pages you have a bunch of files, for example 
migrations (for any db migrations)
admin (if you want to show stuff in the admin area)
apps.py (shows you the class of the config. This will go in our settings file)
models.py (where you create models, e.g. listings will have the title and address and no. of bedrooms)
tests.py
views.py (create methods and link urls to those methods)

**Add app to settings.py**
Go to settings.py (Ctrl + P to find the file)
Add the page to the INSTALLED_APPS 'pages.app.PagesConfig'
You know that it is PagesConfig because that's what appears in apps.py
Once that is saved, Django will then recognise pages as an app

```py settings.py
INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    ...
```

**Install autopep8**
Autopep8 is a tool that automatically formats Python code to conform to the PEP 8 style guide. You should install autopep8 in the virtual environment
$ pip install autopep8

**Create urls.py file for pages app**
Inside the pages folder you should create a new file called urls.py
$ touch pages/urls.py
Enter the newly created file (Ctrl + P urls.py)

# If you want to define a path, you will actually have to bring the path package in
from django.urls import path

```py pages/urls.py
# Bring in the views because the idea is to have a path/url/route that is attached to a method inside the view file. # We want a url for our homepage
from . import views

urlpatterns = [
    path('', views.index, name='index') # The first parameter is '' (the route path / the homepage). In a lot of frameworks you will see '/', but we leave it empty in Django
    # The second parameter is the method we want to connect this to in the view (views.index)
    # The third and final parameter is the name. We set the name here to easily access the path, which we'll call 'index'
]
```

```py pages/views.py
from django.shortcuts import render
# Import
from django.http import HttpResponse

# Write function index with the parameter request
def index(request):
    return HttpResponse('<h1>Success with HttpResponse</h1>')
```

You will need to include pages.urls in the main urls.py
```py btre/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Leave path blank because we want the homepage to appear with nothing
    # include 'pages.urls' (note, you need to bring include in as part of the django.urls package)
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
```

Once you've done that, you should be able to see something happening on localhost:8000.

**Rendering a template**
For testing purposes, we just put html directly into the htmlresponse
```py
return HttpResponse('<h1>Success with HttpResponse</h1>')
```
We actully want to render a template. Therefore we want to create a templates folder and we will create a structure so we can add our HTML to be served

First step is telling Django where to actually look for templates. You can do this in settings.py where the TEMPLATES dictionary is. Go to DIRS and let it know that your templates are in the root
```py btre/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Traversy likes to keep his templates in the route
        'DIRS': [os.path.join(BASE_DIR), 'templates'],
        ...
```

Then go into root and create a folder called templates
It's up to you how you want to structure the templates; Traversy likes to categorise them.
$ mkdir templates && mkdir templates/pages && touch templates/pages/index.html templates/pages/about.html

Now that we have our templates created, we need to go our pages app and go to pages/urls.py and create an about route
```py pages/urls.py
# should something be included here?
urlpatterns = [
    # We can use path because we brought the path package in at the top of this code
    # The first parameter is '' (the route path / the homepage). In a lot of frameworks you will see '/', but we leave it empty in Django
    # The second parameter is the method we want to connect this to in the view (views.index)
    # The third and final parameter is the name. We set the name here to easily access the path, which we'll call 'index'
    path('', views.index, name='index'),
    
    # Create an about route, with the method name also about. We will get an error initially as there is no about method in the views file so we will have to create that in 
    path('about', views.about, name='about')
]
```

To bring in the about page, we won't return an HttpResponse like we did when we were testing. Instead, we actually want to render a template.
We can do this by bringing in render at the top of the page
```py pages/views.py
from django.shortcuts import render
# Import
from django.http import HttpResponse

# Write function index with the parameter request
def index(request):
    return HttpResponse('<h1>Success with HttpResponse</h1>')

# Write function/method about
def about(request):
    return HttpResponse
```

**base layout base.html**
The issue we have at the moment is that when we want a header, js references, css references etc. we will have to repeat on each template (index, about etc). To prevent this needless repetition, we can extend a `base layout`

Ctrl + Shift + 5 (to create a new terminal alongside the terminal running the server)
$ touch templates/base.html

base.html will contain our html head tags and stuff like that.
You create a boilerplate and then in the body, you want to output any template that we extend or that we use to extend this layout.
You will need the jinja syntax for this. Jinja is the template engine that Django uses by default

**Jinja**
Jinga is a templating language for Python, modelled after Django's templates
Jinga uses Curly braces & percent signs. It's like writing PHP inside your HTML.
In VSCode, you can install the Jinja extension. The extension will highlight the code for you, but installing it will knock you out of the environment and will also stop your server
```html
<body>
    {% block content %} {% end block %}
</body>
```

**Loops and Conditionals in Jinja**
Below is an example of a conditional and a for loop in Jinja
```html
{% if listings %}
    {% for listing in listings %}
    <!-- html -->
    {% endfor %}
{% else %}
    <!-- html -->
{% endif %}
```

Now that we have that, whenever we have a template that we want to extend that layout from, we actually have to do two things:
(1) Use tags to say extend
(2) Wrap content with block content

```html templates/pages/about.html
{% extends 'base.html' %}

{% block content %}
<h1>About</h1>
{% endblock %}
```

**Starting Bootstrap with Static Files and Paths**
In order to bring in our Boostrap theme, we need to ask ourselves "How do you handle Static Files in Django?"
This can be a bit confusing...
We have (i) our btre project folder and (ii) our btre theme included in the btre_resources

Within the btre_resources, we have the btre_theme
Within btre_theme, the important folder is 'dist'
Within dist, we have our html files and the assets folder
The assets folder contains all our css, boostrap, js, fonts, images

The key thing we want to do is to bring all that stuff into our application as static assets
To do this, we need to create a static folder within the btre folder
$ mkdir btre/static

We want to put our static files within that static folder (all the css, js and webfonts folders)
We don't want all the images. We will upload the images through the admin area

Inside our main btre project, we have a folder called btre. btre was generated when we ran `$ django-admin startproject btre .` 
We put our static folder inside the project

**Add static root**
Next step is going to our settings file & go to the bottom where we have the STATIC_URL set to '/static/'
We want to add (i) the static_root and (ii) the location of the folder we just created
When you deploy your application you run a command called `collectstatic`. This command goes into all of your applications, and looks for a static folder. It will then take everything out and put it into a root static folder

```py btre/settings.py
# You can call it anything; it doesn't have to be 'static'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
# Set location of folder we just created
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'btre/static')
]
```

**Test the static folder set up**
Run this command. You should get a message saying "X static files copied to _DIR". This command will create a static folder in our root. It has the stuff we put in and also the static admin files
$ python manage.py collectstatic

When we deploy, this is where it will look
Important: You do not want to add /static to your git repo. 

**Linking Static Assets using {% load static %}**
Open up the Boostrap files that we were given at the start of the project and take copies of the important lines of code & paste them into your project
You should be pasting in the links to the static files & also the scripts at the bottom of the page

```html templates/base.html
    <!-- Font Awesome -->
    <link rel="stylesheet" href="assets/css/all.css">
    <!-- Bootstrap -->
    <link rel="stylesheet" href="assets/css/bootstrap.css">
    <!-- Custom -->
    <link rel="stylesheet" href="assets/css/style.css">
    <title>Traversy Real Estate</title>
</head>
<body>
    {% block content %} {% endblock %}

    <script src="assets/js/jquery-3.3.1.min.js "></script>
    <script src="assets/js/bootstrap.bundle.min.js "></script>
    <script src="assets/js/main.js "></script>
</body>
```

This won't work yet because the srcs are incorrect
The way that we reference the static files that we just brought it is as follows
(i)  You need to load static `{% load static %}` at the top of the page 
(ii) You need to re-do all the hrefs as below by adding "{% static 'src' %}"
```html
<!-- before -->
    <link rel="stylesheet" href="assets/css/all.css">
<!-- after -->
    <link rel="stylesheet" href="{% static 'css/all.css' %}">
```
This will actually reference whatever our static folder is and it will look for css/all.css
Therefore these changes will mean that Django will now look in the correct folder (i.e. the static folder)

**Bring over remaining Bootstrap**
Copy over the navbar, the topbar and the footer
These will be on every single page so you want them in base.html

**Partials**
We don't want the base.html to be cluttered up with lots of markup
Therefore, we can create a separate folder in our templates folder called partials
The partials we want to create are the navbar, the topbar and the footer
The naming convention for partials is to use an underscore in front of the name (e.g. _topbar.html)
$ touch templates/partials/_topbar.html

**Bring in Partials**
```html
<!-- Top Bar -->
{% include 'partials/_topbar.html' %}
```

**Bring in the logo**
You are going to continue to get an error because you haven't brought in the logo yet

```html templates/partials/_navbar.html
{% load static %}
...
<img src="{% static 'img/logo.png' %}" class="logo" alt="">
```

**Add html markup**
Continue to copy in the html markup from the Boostrap template
Remember, we will be adding the listings from the admin area. This means that the images will come from somewhere different; they won't come from the static files. We just need some placeholder images for the moment though, which is why we are keeping them there.

When there is stuff that is coming from static, though, we do need to edit it so that Django looks in the static folder.

Important to understand that when we extend it has to be the first line
Therefore, `{% load static %}` has to be below `{% extends 'base.html' %}`

```html templates/pages/about.html
{% extends 'base.html' %}
{% load static %}
```

*Note: A breadcrumb or a breadcrumb trail is a graphical control element frequently used as a navigational aid in user interfaces and on web pages. The term is a reference to the trail of bread crumbs left by Hansel and Gretel*

**Links**
To include a link you need to include the tags {% tags and the key word url 
The word 'index' comes from pages/urls.py. It is the name in the urlpatterns

```html templates/partials/_navbar.html
<a class="nav-link" href="{% url 'index' %}">Home</a>
...
<a class="nav-link" href="{% url 'about' %}">About</a>
```

**Highlighting the Links with conditionals**
We now are going to handle the highlighting of the links. Currently if we go to the 'about' page, 'home' is still active. 
The class of 'active' on the <li> of causing this
We want to change it to make it dynamic so we therefore need to create a bit of clutter by adding a conditonal to the template

Initially it looks like this
```html templates/partials/_navbar.html
<li class="nav-item mr-3">
<a class="nav-link" href="{% url 'index' %}">Home</a>
<!-- <a class="nav-link" href="index.html">Home</a> -->
</li>
```

After a conditional, it looks like this:
```html templates/partials/_navbar.html
<li
    {% if '/' == request.path %}
        class="nav-item active mr-3"
    {% else %}
        class="nav-item mr-3"
    {% endif %}
>
<a class="nav-link" href="{% url 'index' %}">Home</a>
```

We're building a real application and the most logical way of doing it is to create all the templates / all the views in the UI before you move onto the database and setting up models and migrations. We want to make sure that we get the Front End UI complete before anything else.

## === Nine Steps to Setting up an App === ## 
**1 Create Listings and Realtors Apps through startapp**
We want to create listings and realters apps. They are going to be similar to the pages app in terms of set up (i.e. we use startapp to create them)
$ python manage.py startapp listings
$ python manage.py startapp realtors

The listings app is going to consist of the (i) listings page, (ii) the single listings page and (iii) the search page
Realtors is just for the model; we're not going to have any templates or views. It's just to be able to add realtors through the admin area and then form a relationship between the realtor and the listing.

**2 Add listings templates**
Note that the listings.html is for all of the listings; listing.html is for one listing
$ mkdir templates/listings/ && touch templates/listings/listing.html templates/listings/listings.html templates/listings/search.html

For listings, we will have some urls that it will connect to. That means that we are going to have to create its own urls.py
$ touch listings/urls.py

**3 Create listings urls**
```py listings/urls.py
from django.urls import path
from . import views

# If we leave the path empty '', it pertains to just /listings
urlpatterns = [
    # We want this to call the index method inside of the listings views file. We give it a name 'listings'
    path('', views.index, name='listings'),
    # We want the single listing to look something like /listings/23 (with 23 being the id)
    # Therefore, we need to include a parameter in our url. We do this by using angle brackets <> and the type (int) and then what we want to call it. That is how we will access our parameter from within the view method. The name of the method will be views.listing
    path('<int:listing_id>', views.listing, name='listing'),
    # Putting in search means that it will be listings/search. The reason we don't put listings/search here is because we are going to link this to the main urls.py and tell it that anything that has listings/ should look at this file
    path('search', views.search, name='search')
]
```

**4 Edit the main project (btre) urls.py**
We want to do the same thing as we did with our pages app by adding a path 
```py btre/urls.py
urlpatterns = [
    # Leave path blank because we want the homepage to appear with nothing
    # include 'pages.urls' (note, you need to bring include in as part of the django.urls package)
    path('', include('pages.urls')),
    # Create listing. Anything that is listings slash is going to go to listings.urls
    path('listings/', include('listings.urls')), `you are including this line here`
    path('admin/', admin.site.urls),
]
```

**5 Add the newly installed apps to settings.py**
It's easy to forget the step in which you have to go to the settings.py file and add to installed apps. *Make sure that you write 'apps' not app*
```py btre/settings.py
INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
```

**6 Test that urls are set up correctly in views.py**
In our urls.py in listings we have index, listing and search. We need to create all of these in the views.py within listings.
A good step now is to return an HTTP response just so you know that everything is set up correctly

```py listings/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Success1 with HttpResponse</h1>') `temp line just to test`
```

**7 Create view methods**
Once you've tested with HttpResponse, you can add the routes to the view templates
```py listings/views.py
def index(request):
    # render takes in two things: (i) the request itself and (ii) the location of the template
    return render(request, 'listings/listings.html')
    # return HttpResponse('<h1>Success1 with HttpResponse</h1>')

def listing(request):
    return HttpResponse('<h1>Success2 with HttpResponse</h1>')

def search(request):
    return render(request, 'listings/search.html')
```

**8 Edit the html within the templates**
Once you have the urls successfully set up, you can edit the html in the templates
Note that with listings, you won't see the images as they will come from the Admin area. There is no point in putting a static image here for show as we will be adding the admin functionality later on

```html listings.html
{% extends 'base.html' %}

{% block content %}
<!-- include html here -->
{% endblock %}
```

**9 Add breadcrumbs and highlighting**
Add the link to the homepage
```html listings.html
<li class="breadcrumb-item">
<!-- Remove href and add url -->
<!-- <a href="index.html"> -->
<a href="{% url 'index' %}">
    <i class="fas fa-home"></i> Home</a>
</li>
```

Add the conditional that will highlight the page you are on
```html templates/partials/_navbar.html
<li 
{% if 'listings' in request.path %}
    class="nav-item active mr-3"
{% else %}
    class="nav-item mr-3"
{% endif %}
>
<a class="nav-link" href="{% url 'listings' %}">Featured Listings</a>
</li>
```

**Architecture of the listings page**
When we create the database and the listings model, we will then reach into the database and pass the listings into the template & then we we will loop through the listings and output one of the divs. This means that we won't have all this markup in the listings.html file

## ===Moving on to the Database=== ##
**Install PostgreSQL**
PostgreSQL is a very powerful relational database which pairs well with Django. It is similar to mySQL or Microsoft SQL server in the way that they are relational databases that use Structural Query Language. With Django we don't have to write raw SQL queries. Instead we have a higer level ORM (Obejct Relational Mapping) that deals with fetching data, inserting data and so on.

To install PostresSQL locally, go to postgresql.org, download, windows & download the graphical installer
*For steps and more info on postgreSQL, go to the sql crib*

**Install Psycopg**
Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
Psycopg 2 is mostly implemented in C as a libpq wrapper, resulting in being both efficient and secure.
https://pypi.org/project/psycopg2/

To install psycopg, run these commands:
$ pip install psycopg2
$ pip install psycopg2-binary

**Implementing Postgres with our Django app**
To use postgres we need to define our parameters in the settings.py file
We also need to install a couple of packages which act as drivers to connect to postgres

Make sure you are in your venv
$ source ./venv/Scripts/activate && pip freeze

Set up parameters in settings.py

```py settings.py
DATABASES = {
    # Set up parameters including driver, username & password
    # First step is changing sqlite3 to postgres
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'btredb',
        'USER': 'postgres',
        'PASSWORD': 'Medi13!',
        'HOST': 'localhost'
    }
}
```

**Run migrations**
We have some unapplied migrations. A migration is a file that tells the database what to do as far as setting up tables, data, columns etc. Django has default migrations for admin area, authentication etc. The migrations files are already set up. They just haven't been run yet. Therefore, now we want to run those migrations.
First step is to stop the server with Ctrl+C

We will create our own migrations for the listings and realtors, but to run the current migrations that are already ready, you run this command
$ python manage.py migrate

To test, you can jump into pgadmin4 and have a look
Go to Databases => btredb => Schemas => Tables
You should now have a bunch of tables (e.g. auth_user, django_session)

If you now run the server again, you will see that you no longer have the errors highlighting that you haven't performed the migrations yet.

**Planning The Schemas**
Before we jump into code, you should always map out the schemas based on the requirements we got given.
We are going to have three separate tables
(1) Listing => the model name is singular
(2) Realtor
(3) Contact => Any inquiry that's made should be saved in the database in a contact table

The first thing you should always do is add an ID. Every table needs an ID column. With postgres, that id will get put in automatically and there will be auto increment

The schema can be found at schemas.md. Now that we have that file, when we create the models in Django we want to model it after that file and all of the fields.

==**Create Listing Model**==
Ids
The id you don't have to start because it will be automatic

Model field Reference
It is much easier to set up our database using a model rather than going into the postgres shell or pgadmin.
When we set up our fields, we need to give them certain types
Charfield is the one we will use the most as this will be for stuff like 'title', 'address' and 'city'
(PostgreSQL specific model fields)[https://docs.djangoproject.com/en/3.0/ref/contrib/postgres/fields/]

Everytime you create an app, a models.py will be created

TextField is a large text field. The default form widget for this field is Textarea. If you specify a max_length attribute, it will be reflected in the TextArea widget of the auto-generated form field. However, it is not enforced at the model or database level. Use CharField for that. You don't actually have to have a max_length though

CharField is for small to large-sized strings. For large amounts of text use TextField. CharField has one extra required argument (max_length). The max_lenght is enforced at the database level and in Django's validation using MaxLengthValidator

IntegerField is for values from -2147483648 to 2147483647

BooleanField is a true/false field

FloatField is for float instances in Python. FloatField class can get mixed up with DecimalField

DateTimeField is a data represented in Python by a datatime.time instance. If you want to use the current date and time, you will need to current datetime package

**Blank=True**
Blank=True means that this field is optional
If we're in the admin area and we put in a listings without a description, we won't get an error
```py models.py listings
description = models.TextField(blank=True)
```

**DecimalField**
If you try to add a non-nullable field without a default, you will get an error on migration
Therefore, you need to include either a default value or you can make it optional

```py
#You can either provide a default value to the field
high52 = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
#or you can make it optional
high52 = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
```

**DecimalField or FloatField**
Both FloatField and DecimalField both represent real numbers, but in different ways.
FloatField uses Python's float type internally, while DecimalField uses Python's Decimal type
DecimalField must define a 'decimal_places' and a 'max_digits' attribute
FloatField does not do smart rounding as can cause round off errors because of how they are stored in hardward

```py
bathrooms: modes.DecimalField(max_digits=2, decimal_places=1) # We actually want this to be a decimal not an integer`
```

**Images and ImageField**
Photos are strings in the database but with Django we have different types of fields (e.g. ImageField)
Inside the ImageField you want to define where the images get uploaded to
In Django, there is a media folder, and we will set that up; anything we upload as far as images or files in the admin area is going to go into that media folder
Within ImageField, we want to define the folder that we want inside of that media folder
If we want each photo to go into a folder structure of the date (the year, the month and the day)

```py
class ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
upload_to='photos/%Y/%m/%d/')
```

**Pillow (Python Imaging Library)**
Note that you will need the dependency Pillow to actually use ImageField
Pillow is a PIL fork. PIL stands for Python Imaging Library

$ source ./venv/Scripts/activate && pip freeze `easier way to do this is with will be with Ctrl + R + activate`
$ python -m pip install --upgrade pip
$ python -m pip install --upgrade Pillow

*note that -m means that you are using the __main__.py script inside the pip package

**Pick Field that will be main field to be displayed**
We need to pick a field that will be the main field to be displayed. It probably makes sense for that field to be the title in this case
In this case, title will now override the default name for any objects in this class

```py models.py listings
def __str__(self):
    return self.title
```

**Dunder Methods**
Dunder methods (double underscore) method marks them as a core Python thing. Dunder means Double Under (underscore). They are commonly used for operator overloading (e.g. __init__, __add__, __len__, __repr__ etc)

**Create Realtors Model**
The Listings Model and the Realtors Model are going to go hand in hand; inside the Listings model, we have a foreign key of realtor that will be linked to the Realtor model

We have now created the Listing and the Realtor models. We now want the stuff in the database. At the moment it is not in the database even though we have saved the model. Therefore, we need to create a migration and then run it.
$ source ./venv/Scripts/activate && pip freeze `easier way to do this is with will be with Ctrl + R + activate`
$ python manage.py makemigrations `this runs all the migrations`
$ python manage.py makemigrations listings `in case you just want to run one`

makemigrations will create a file. It won't do anything in the database; instead, it will simply create the file that we can run to then update the database

In the listings folder, there is a migrations folder. makemigrations will create a file that will be put in the file
The makemigrations command creates a file called 0001_initial.py inside the migrations folders

**Test Migration**
This shows you the SQL; you can look through the result to check that everything has been migrated as expected.
$ python manage.py sqlmigrate listings 0001

It is called listings_listing because it is the name of the app, then underscore, then the name of the model. It then gives it an id. serial means it is auto increment
varchar is the postgres data type. charfield is the Django model type

Note, if you made a mistake with makemigrations, you could try doing it again by deleting 0001_initial.py and the corresponding file inside the __pycache__

**Do the migration**
This command will actually change the database by adding the tables
$ python manage.py migrate

You can check this
C:\Program Files\PostgreSQL\12\pgAdmin 4\bin\pgAdmin4.exe

==**Admin Area**==
The admin area according to Traversy is one of the greatest features of Django. It is great if you are a freelancer & you don't want to create a custom admin area
Make sure you have your server running and the go to localhost:8000/admin
The admin section has been here all the time however there is no way of logging in at the moment

Therefore, we should create a super user
Ctrl + ' to switch to console
Ctrl + Shift + 5 to split the console screens so that you have python running in one & a normal bash window running on the other

$ source ./venv/Scripts/activate && pip freeze
$ python manage.py help `look at commands`
$ python manage.py createsuperuser

username: ralph
email address: ralphpayne@gmail.com
passwords: 123456
bypass p/w validation: y

Now you can log into the admin area.
Here we can manage users and groups

This is good for allowing users into the back office if you want (by checking staff status)

**Register Listing for Admin area**
listings/admin.py is where we can customize admin stuff for the listings app
Below we want to register listing for the admin area
To do this, we need to bring in our models

```py listings/admin.py
from .models import Listing
# def register(self, model_or_iterable, admin_class=None, **options):
admin.site.register(Listing)
```

Test by going back to the admin area. You should now be able to add listings
Note that required fields are dark
Is published is a checkbox

This is outstanding functionality to have out of the box. This is why Django is brilliant.

**Define Media Path (where photos will be uploaded)**
We need to define some stuff for the media folder where the photos will be uploaded

```py btre/settings.py
# Media folder settings
MEDIA_PATH = os.path.join(BASE_DIR, 'media')
#Set media url
MEDIA_URL = '/media/'
```

**Edit urls to include media url and media root**
We also need to edit the main urls.py

```py btre/urls.py
from django.contrib import admin
from django.urls import path, include
# We need to bring these two in for the media files to show up in the front end
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Leave path blank because we want the homepage to appear with nothing
    # include 'pages.urls' (note, you need to bring include in as part of the django.urls package)
    path('', include('pages.urls')),
    # Create listing. Anything that is listings slash is going to go to listings.urls (i.e. the urls.py in the listings app)
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
    # If we don't include this setting, things won't show up correctly
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Add Data to the site**
Add dummy data to the site (e.g. Realtor etc.)
The reason why see the name of the Realtors under the realtors page is because we specified this line here
If we hadn't added that line, the admin site would say something like realtor object 1 or something like that
It also means that on the listings page, the dropdowns of realtors shows the name as well
Note that all the media files are now been stored in the photos folder

```py realtors/models.py
def __str__(self):
        return self.name
```

**Customize the Admin area**
Change Django Administration
You need to create a file
$ mkdir templates/admin && touch templates/admin/base_site.html

We now extend the admin template so we can add blocks

```html templates/admin/base_site.html
<!-- We want to extend this template -->
{% extends "admin/base.html" %}
<!-- We load static so that we can bring in the logo -->
{% load static %}

{% block branding %}
    <h1 id="head">
        <img src="{% static 'img/logo.png' %}" alt="BT Real Estate" class="brand_img" height="50" width="80">
            BT Real Estate
    </h1>
{% endblock %}
```

For CSS, we need to add another block called extrastyle & create a new css file
There are two static folders. Make sure you create it in the btre one
$ touch btre/static/css/admin.css

```css btre/static/css/admin.css
/* Edit the header. We know it has an id of header from going from Chrome tools */
#header {
    height: 90px;
    background-color: #10284e; /* dark blue */
    color: #fff;
}

/* Take the branding id & go into the h1 */
#branding h1 {
    color: #fff;
}
```

**Customize Listings Admin Page**
Customize tables etc.
We can customize a lot without actually having to go into the Django admin code. You don't want to be doing that. We have a lot of methods that allow us to customize.
To do this, we need to go to our listings app then admin.py
This is where we registered the model

```py listings/admin.py
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

admin.site.register(Listing, ListingAdmin)
```

**Customize Realtors Admin Page**
We also want to make some changes to Realtors with the admin.py 
```py realtors/admin.py
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
```

===**Front End Site**===

**Take listings from database and pass them into template**
We now want to start to fetch data from the database and display it in the front-facing website
We want to fetch our listings using our model and then we insert the data into our template. Once we've done that, we can loop through and output the listings that are in the database
The first step is bringing in the listings model into listings/views.py. Note, we can bring in any model we want into any file we want and we can list it.

```py listings/views.py
# Bring in our model
from .models import Listing

# Write function index. index will be the main listings page
def index(request):
    # render takes in two things: (i) the request itself and (ii) the location of the template
    return render(request, 'listings/listings.html')
    # return HttpResponse('<h1>Success1 with HttpResponse</h1>')
```

*Defintion: MVC: Model View Controller => a Model View Controller is a software design pattern commonly used for developing user interfaces which divides the related program logic into three interconnected elements*

If you've used any view rendering or MVC related framework in any language, you'll know that you can pass in values into a template. In Python, we do that with a dictionary. This is a way of passing values from a file like views.py into a template like templates/listings.html. Common practice is to create a variable with the dictionary rather than passing in the actual dictionary as a parameter. We then pass in the variable we created.

```py listings/views.py
def index(request):
    # Create variable called listings and set it to the model name called Listing. This variable will get passed into the dictionary 'context'
    listings = Listing.objects.all()

    # Create variable that we will pass into the render function
    context = {
        # The key is 'listings'; the value is the variable you created above (all the objects from the model Listing)
        # A common mistake here is to write 'listing' instead of 'listings' or the other way round. A lot of the typos are because you have written singular when it should be plural or you have writting plural when it should be singular
        'listings': listings
    }

    # Pass the context into the template
    return render(request, 'listings/listings.html', context)
```

**Loop throug listings in template**
You now want to loop through the listings and you want to output each listing with dynamic variables

```html template/listings.html
<div class="row">
    {% if listings %}
        {% for listing in listings %}
            <div class="col-md-6 col-lg-4 mb-4">
                <!-- insert html here -->            
            </div>
        {% endfor %}

    <!-- The else covers if there are no listings in the database -->
    {% else %}
        <!-- col-md-12 will take up whole row -->
        <div class="col-md-12">
            <p>No Listings Available</p>
        </div>
    {% endif %}
</div>
```

**o**
Replace hardcoded data with dynamic values
Right now, we are outputting static html for each listing; it's the same thing for each object we are pulling from the database
To replace the data, we can use the template syntax of double curly braces {{ }}
When we looped through, we said for listings in listing. listings is what we passed into the template and we're saying for every instance or iteration, we are going to call it listing
For example, if we want the title, we will write {{ listing.title }}
We can get all the names from the schema in listings/models.py

```html listings.html
<div class="listing-heading text-center">
    <h4 class="text-primary">{{ listing.title }}</h4>
    <p><i class="fas fa-map-marker text-secondary"></i> {{ listing.address }}</p>
</div>
```

**Displaying Images**
Django makes it very easy to display images. The models.ImageField that we used means that we can extract the url and put it into the src

```html listings/html
<!-- Overwrite the static below -->
<!-- <img class="card-img-top" src="assets/img/homes/home-1.jpg" alt=""> -->
<img class="card-img-top" src="{{ listing.photo_main.url }}" alt="">
```

**django.contrib.humanize**
When it comes to numbers, we want proper formatting so we can use an app called humanize
Humanize has methods called intcomma, intword, natural day. We want to use intcommma
[Humanize documention](https://docs.djangoproject.com/en/3.0/ref/contrib/humanize/ "Humanize Docs")

In order to use humanize, we need to add it to INSTALLED_APPS in settings.py; we also need to use {% load humanize %} to load it in the template and then you will use a pipe character | and intcomma

```py btre/settings.py
INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    ...
    # Install humanize for intcomma
    # https://docs.djangoproject.com/en/3.0/ref/contrib/humanize/
    'django.contrib.humanize',
]
```

```html templates/listings/listings.html
<!-- Load Humanize -->
{% load humanize %}
...
<span class="badge badge-secondary text-white">$ {{ listing.price | intcomma }}</span>
```

**Timesince with Humanize**
Timesince with humanize
```html 
<i class="fas fa-clock"></i>{{ listing.list_date | timesince }}</div>
```

**Relationship between listing and realtor**
Since we have a relationship between the listing and the realtor, we can just include realtor as so: {{ listing.realtor }}
Whatever we put in the model for the realtor in realtors/models.py under return self.name will be displayed

```py realtors/models.py
class Realtor(models.Model):
    # The id you don't have to start because it will be automatic
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    ...
    # Just like with listings, we need a main field; This field will be the Realtor's name
    def __str__(self):
        return self.name
```

```html listings/html
<div class="row py-2 text-secondary">
<div class="col-12">
    <i class="fas fa-user"></i>{{ listing.realtor }}</div>
</div>
```

**Create dynamic href to individual listing page**
We have already set up the route for single listings in listings/urls.py
The url is listings/<'whatever the id is'>

```py listings/urls.py
urlpatterns = [
    path('', views.index, name='listings'),
    # Route for single listings
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]
```

Therefore, we now want the 'More Info' button to direct the user to the route of the single listing. We will need url tags for this

```html listings.html
<!-- legacy code below -->
<a href="listing.html" class="btn btn-primary btn-block">More Info</a>
<!-- dynamic url -->
<a href="{% url 'listing' listing.id %}" class="btn btn-primary btn-block">More Info</a>
```

**Render individual listing page**
There is one more configuration we need to change

In listings/urls.py, we pass in '<int:listing_id>' and this goes to the listing method
The listing method is in listings/views.py. When you pass a parameter like that, you also need to pass it into the method

```py listings/views.py
def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    # render takes in two things: (i) the request itself and (ii) the location of the template
    return render(request, 'listings/search.html')
```

Therefore, we need to update views.py
```py listings/views.py
def listing(request, listing_id):
    return render(request, 'listings/listing.html')
```

**Add a paginator to index method**
Adding Pagination to the Application
https://docs.djangoproject.com/en/3.0/topics/pagination/

First step is adding a paginator to the index method within listings/views.py

```py listings/views.py
# Bring in the paginator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Bring in our model
from .models import Listing

def index(request):
    # Create variable called listings and set it to the model name called Listing. This variable will get passed into the dictionary 'context'
    listings = Listing.objects.all()
    # Include paginator & pass in listings (variable above from the database) & the number of listings we want per page
    paginator = Paginator(listings, 3) # Show 6 listings per page
    # Create variable called page from the get request; when the user is on page 2, there will be a url paramater that will say page=2
    page_number = request.GET.get('page')
    # Pass the page into Paginator
    paged_listings = paginator.get_page(page_number)
```

We also need to change what we pass into the context. Previously we passed in a key: value pair of 'listings': listings. We now want to change that to 'listings': paged_listings

```py
context = {
    'listings': paged_listings
}
```

**Previous arrow for pagination**
We have now fetched the right data from the database. The next step is to display it the right way

The way that Django displays pagination is not aestecially pleasing on the eye. Therefore, we should use Bootstrap, which uses the class 'page-item'. Every page has a class of 'page-link'.

First, wrap the whole block in an if statement which checks to see if we actually need pagination (i.e. you might only have 6 items total and want to display 6 per page)

Pagination is a notoriously difficult thing to do, but Django makes is surprisingly easy. It's one of the easier frameworks to deal with pagination

```html listings.html
{% if listings.has_other_pages %}
    <ul class="pagination">
        <!-- If there is a previous page, then we want a link to the previous and also left facing arrows (&laquo) -->
        {% if listings.has_previous %}
            <li class="page-item">
                <!-- Include left facing arrows with &laquo -->
                <a href="?page={{listings.previous_page_number}}" class="page-link">&laquo;</a>
            </li>
        {% else %}
            <li class="page-item disabled">
                <!-- Don't need an href if there are no previous pages -->
                <a class="page-link">&laquo;</a>
            </li>
        {% endif %}
        <!-- Loop through page range -->
        {% for i in listings.paginator.page_range %}
            <!-- If the listings number is equal to the page, then display an active link -->
            {% if listings.number == i %}
                <li class="page-item active">
                    <a class="page-link">{{i}}</a>
                </li>
            {% else %}
            <!-- If the listings number is not equal to the page, then display the number, but not active -->
            <!-- The href has a page query which will go to the value of i -->
                <li class="page-item">
                    <a href="?page={{i}}" class="page-link">{{i}}</a>
                </li>
            {% endif %}
        {% endfor %}
    </ul>
{% endif %}
```
You can now test this by reloading the page & looking at the url parameters

**Next arrow for pagination**
Now we want to add a next button
We do that right below the endfor loop & we can just copy the code we wrote for endprevious
https://www.toptal.com/designers/htmlarrows/
Instead of double left pointing arrows (HTML entity &laquo), we use right pointing arrows (HTML entity &raquo)

```html
{% if listings.has_next %}
    <li class="page-item">
        <a href="?page={{listings.next_page_number}}" class="page-link">&raquo;</a>
    </li>
{% else %}
    <li class="page-item disabled">
        <a class="page-link">&raquo;</a>
    </li>
{% endif %}
```
To test, you can go to listings/views.py and change the number of listings you want per page

**Order_by**
We want to order by date. We can change this is listings/views.py
```py listings/views.py
# change this
listings = Listing.objects.all()
# to this
listings = Listing.objects.order_by('-list_date')
```

**Filter and only show published items**
We also want it so that if the listing is unpublished in the back-end, it doesn't appear in the front-facing site
We can chain that onto the same line. You just filter by the name of the model field
```py listings/views.py
listings = Listing.objects.order_by('-list_date').filter(is_published=True)
```

**Make Home Page dynamic**
We now want to make the home page dynamic as well. We need to switch our focus to pages/views.py and pages/index.html & repeat the tasks we did for the listings app
Even though we are in the pages app, we can actually get any model we want.

```py pages/views.py
# Bring in Listings model
from listings.models import Listing

# Write function index
def index(request):
    # We use the same parameters as we did in listings/views.py but this time we also add [:3] to specify that we only want three listings
    latest_three_listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': latest_three_listings
    }
    # Pass the context into the index template
    return render(request, 'pages/index.html', context)

```

**Loop through listings in template**
Now that we have passed the context into the index.html, all we need to do is loop through those listings and display them in the template
Note, that you need to load humanize {% load humanize %} as you did with listings 

```html templates/pages/index.html
{% if listings %}
    {% for listing in listings %}
    <!-- html -->
    {% endfor %}
{% else %}
<!-- html -->
{% endif %}
```

**Pull data from database for realtors**
Now, we edit the about page and bring in the information for realtors as well as making the seller of the month dynamic

```py pages/views.py
def about(request):
    # Bring in all realtors from the database
    realtors = Realtor.objects.order_by('-hire_date')
    context = {
        'realtors': realtors
    }
    return render(request, 'pages/about.html', context)
```

**A note on query sets in Django**
https://docs.djangoproject.com/en/3.0/ref/models/querysets/
The negative sign (-) before a key (e.g. hire_date indicates a descending order when you use the order_by method

**Get MVP**
Initially I did the logic for seeing who is mvp through the actual about template. This is slightly less efficient that pulling the mvp in the views.py

**Loop through realtors**
Check the model (realtors.models.py) for the attribute names and then Loop through the realtors on templates/pages/about.html
The code below shows the markup for displaying seller of the month. There is also code at the bottom of about.html.
To test, you can go to the admin section and unclick the mvp checkbox for the realtor who is current MVP. This should make the card disappear.

```html templates/pages/about.html
<div class="col-md-4">
    {% if mvp_realtors %}
        {% for mvp_element in mvp_realtors %}
            <div class="card">
                <img class="card-img-top" src="{{ mvp_element.photo.url }}" alt="Seller of the month">
                <div class="card-body">
                <h5 class="card-title">Seller Of The Month</h5>
                <h6 class="text-secondary"> {{ mvp_element.name }} </h6>
                <p class="card-text"> {{ mvp_element.description }} </p>
            </div>
            </div>  
        {% endfor %}
    {% endif %}
    <!-- We don't need an else because if there are no MVPs, then we don't display anything -->
</div>
```

**Display Team of Realtors**
A good tip is to start with the logic and then wrap the html within the logic you have already set up
```html templates/pages/about.html
{% if realtors %}
    <!-- html here -->
{% else %}
    <!-- html here -->
{% endif %}
```

```html templates/pages/about.html
{% if realtors %}
    {% for element in realtors %}
        <div class="col-md-4">
        <img src="{{ element.photo.url }}" alt="" class="rounded-circle mb-3">
        <h4>{{ element.name }}</h4>
        <p class="text-success">
            {% if element.is_mvp %}
            <i class="fas fa-award text-success mb-3"></i>
            {% endif %}
                Realtor</p>
        <hr>
        <p>
            <i class="fas fa-phone"></i>{{ element.phone }}</p>
        <p>
            <i class="fas fa-envelope-open"></i>{{ element.email }}</p>
        </div>
    {% endfor %}
<!-- The else covers the situation in which there are no realtors in the database -->
{% else %}
    <div class="col-md-12">
        <p>No Realtors Available</p>
    </div>
{% endif %}
```

**Display Images**
Important to note the syntax for displaying images in Django
You need to remember the .url suffix

```html
<img class="card-img-top" src="{{ listing.photo_main.url }}" alt="">
```

**Create Single Listing Page**
The route is already set and the template is displaying. We now want to display the right markup inside templates/listings/listing.html
(01) Copy the static html from btre resources
(02) Extend the base html with {% extends 'base.html' %}
(03) Wrap all markup in a block {% block content %} ... {% endblock %}
(04) Load humanize {% load humanize %} after you extend the base.html and before you create the block
(05) In listings/views.py, import get_object_or_404 from django.shortcuts `from django.shortcuts import render, get_object_or_404`
(06) In listings/views.py grab the data with one_listing = get_object_or_404(Listing, pk=listing_id)
(07) Change the static html in listing.html to dynamic html
(08) Update the links from <a href="index.html"> to <a href="{% url 'index' %}">Home</a>. You never want an href to an html page; that's just for the theme
(09) Edit links for breadcrumbs <li class="breadcrumb-item"> <a href="{% url 'listings' %}">Listings</a>
(10) Change photos from <img src="assets/img/homes/home-1.jpg" alt="" class="img-main img-fluid mb-3"> to <img src="{{ one_listing.photo_main.url }}" alt="" class="img-main img-fluid mb-3">
(11) Update the other photos (note that the lightbox needs two references to the same src; it's how it chooses the images) `see code below`
(12) Include logic to cover scenario if listing does not have smaller photos associated with it {% if one_listing.photo_1 %}
(13) Include realtor photo <img src="{{ one_listing.realtor.photo.url }}" alt="{{one_listing.realtor}}" class="rounded-circle mb-3">. As we have the relationship between listings and realtor, we can include any field and we can therefore access the realtor's photo url

```html templates/listings/listing.html
{% if one_listing.photo_1 %}
    <div class="col-md-2">
        <a href="{{ one_listing.photo_1.url }}" data-lightbox="home-images">
            <img src="{{ one_listing.photo_1.url }}" alt="" class="img-fluid">
        </a>
    </div>
{% endif %}
```

```py listings/views.py
def listing(request, listing_id):
    # Instead of Listings.objects, we use get_object_or_404(), which calls get() on a given model manager, but raises Http404 instead of the model's DoesNotExist exception
    # If you do not do this, the app could crash if a user searched for a listing in the url paramater that did not exist
    # https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/
    # You pass in two things (1) is the model (2) is the primary key (pk)
    # In listings/urls.py, you can see that the listing_id is passed through the url => path('<int:listing_id>', views.listing, name='listing')
    # You also need to bring in get_object_or_404 at the top (it's from django shortcuts)

    one_listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'one_listing': one_listing
    }
    return render(request, 'listings/listing.html', context)
```


**i**
SEARCH FORM

**Prepare Search Template**
Shorten up all the markup we have by putting it in a Python dictionaries and then importing them and looping through them
Ctrl + ' => Switch to Terminal View
Ctrl + Shift + 5
$ touch listings/choices.py
Ctrl + P + choices.py
Get data from https://github.com/bradtraversy/btre_project/blob/master/listings/choices.py

In choices.py, we have three dictionaries: bedroom_choices, prices_choices, state_choices
Each one has a key: value pair. The key is going to be used for the value attribute. So, if you take prices as an example, the actual value that will be searched in the database will be '100000' and $100,000 will be displayed to the user. With states, 'AK' will be searched in the database and 'Alaska' will be displayed to the user

Then go to pages/views.py because we want the search bar on the homepage
Import the dictionaries: `from listings.choices import bedroom_choices, price_choices, state_choices`
Pass the dictionaries into the index.html through context
Loop through the dictionaries within templates/pages/index.html

```py pages/views.py
...
from listings.choices import bedroom_choices, price_choices, state_choices
...

def index(request):
    ...
    context = {
        'listings': latest_three_listings,
        # Pass in the dictionaries for the search bar
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
    }
    return render(request, 'pages/index.html', context)
```

```html templates/pages/index.html
<div class="col-md-4 mb-3">
    <label class="sr-only">State</label>
    <select name="state" class="form-control">
    <option selected="true" disabled="disabled">State (All)</option>
        <!-- Loop through dictionary -->
        {% if state_choices %}
            {% for key, value in state_choices.items %}
                <option value="{{ key }}">{{ value }}</option>
            {% endfor %}
        {% endif %}
    </select>
</div>
```

**dictionary.items() method**
Note that above, you are looping through the dictionary and returning both the key and the value.
To do this, you need to use the `items() method`. This method lets you loop through the key-value pairs one at a time and gives you access to both the keys and the values
For more info, go to [iterate through dictionary](https://realpython.com/iterate-through-dictionary-python/)

A common mistake is to forget to add .items to the dictionary

**Handling the Submit button on the Search form**
Currently, pressing submit will take you to a page that doesn't exist

01 Change the action on the form so that it goes to url search <form action="{% url 'search' %}">
02 Within listings/urls.py, you can see that we already have the path set up `(path('search', views.search, name='search')`. This means that when we go to urls search, urls.py will call the search method
03 In listings.views.py, you can see the actual search method `return render(request, 'listings/search.html')`. This shows that calling the search method will take you to the listings/search.html template
04 If you put values into the form on index, those values will appear as url parameters. They are get request values.
05 Paste the html markup into listings/search.html and extend the base layout `{% extends 'base.html' %}`. Bring in humanize `{% load humanize %}`
06 Pull the fields from choices.py by bringing in the search options into listings/views.py `from .choices import bedroom_choices, price_choices, state_choices`
07 Add context to the search method in listings/views.py. Include bedroom_choices, state_choices & price_choices `see below`
08 Loop through the different dictionaries just like you did when creating the index.html template

```html templates/listings/search.html
<!-- Before -->
<form action="search.html">
<!-- After -->
<form action="{% url 'search' %}">
...
<button class="btn btn-secondary btn-block mt-4" type="submit">Submit form</button>
</form>
```

```py listings/views.py
def search(request):
    
    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
    }

    return render(request, 'listings/search.html', context)
```

**Search Form Filtering**
We want to create a query so that when the user puts some search fields into the form, the inputs will get caught in the search method and the app will make queries to the database
This is known as Search Form Filtering

01 The first thing we will need to do when the user submits a query is to check if that field (e.g. 'pool') exists. Then we are going to want to pull it out of the request, put it into a variable and then base our QuerySet based on that variable. We will want to filter by the query.
02 Within listings/views.py, you want to start a queryset_list on its own is just like the listings page; it will get all of the listings `queryset_list  = Listings.objects.order_by('-list_date')` 
03 We need to add filters for the search
04 For the moment we will keep it like this within adding a filter just so we can focus on getting our template set up
05 Therefore, the next step is to pass the queryset_list into the context `'listings': queryset_list`
06 We now want to render what we are getting from context in the listings/search.html template
07 So, you should copy the markup from templates/listings.html into templates/search.html with the conditional and the for loop so that the actual results from the database get rendered.
Eventually, this will be filtered, but for now it should show all the listings

```py listings/views.py
def search(request):
    
    # Create QuerySet list which we can build onto
    # class QuerySet(model=None, query=None, using=None, hints=None)
    # https://docs.djangoproject.com/en/3.0/ref/models/querysets/
    queryset_list  = Listing.objects.order_by('-list_date')

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': queryset_list
    }

    return render(request, 'listings/search.html', context)
```

**Create the filter for keywords**

```py listings/views.py
def search(request):
    
    # Create QuerySet list which we can build onto
    # class QuerySet(model=None, query=None, using=None, hints=None)
    # https://docs.djangoproject.com/en/3.0/ref/models/querysets/
    queryset_list  = Listing.objects.order_by('-list_date')

    # Comment all the fields
    # Keywords
    # Check if it exists by  
    # When you make a request with this form, it is a get request and you can actually test to see if it exists
    if 'keywords' in request.GET:
        # If it exists, we create a variable & we get the actual form value
        # Note that you need square brackets
        keywords = request.GET['keywords']
        # We then do another if to check that it is not an empty string
        if keywords:
            # Set a filter on our query_set_list and we search the description for any keywords that are typed into the keywords box
            # We are doing a search that is not an exact match (i.e. we're not looking for alabama = alabama, we're looking for one word inside a block of text)
            # Therefore, we need to use icontains (icontains is a case-insensitive containment test)
            # To test, find a word in one of the property descriptions and perform a search on it
            # Once you've tested successfully, you also are going to need to change <form action="search.html"> to <form action="{% url 'search' %}">
            # Note that if you now search for nothing, you will get all the listings
            queryset_list = queryset_list.filter(description__icontains=keywords)
```

**Create the filter for city**
'city' is also a text field, but with city we want to match the exact text string (i.e. we're looking for chicago & we want the exact match. not like when you search for 'pool' in the description field

```py listings/views.py
# 'city' is also a text field, but with city we want to match the exact text string (i.e. we're looking for chicago & we want the exact match. not like when you search for 'pool' in the description field
# City
if 'city' in request.GET:
    # Create a variable called city
    city = request.GET['city']
    # Check that city is not an empty string
    if city:
        # The difference here is that you want an exact match instead of just contains. Ergo, you should use iexact instead of icontains. iexact is a case-insensitive exact match
        # If you wanted to make it case sensitive, then you should use 'exact' instead of 'iexact'
        # https://docs.djangoproject.com/en/3.0/ref/models/querysets/
        # You should now test the localhost:8000 by performing a query for city
        queryset_list = queryset_list.filter(city__iexact=city)
```

**Adding more fields**
If you ever want to add a field, you can just add that field to the query set
Note, you can actually look for more than one field (i.e. you could perform a query of city and state together)
Adding more fields is as simple as copying and then "doing a Control + D" to replace the values

**iexact, lte, gte**
With bedrooms, we don't want to do an exact match. If someone searches for 4 bedrooms, you want them to get everything up to four bedrooms.
Instead of iexact, we will use lte (less than or equal to <=)

```py listings/views.py
if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
        queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
```

**name attribute of select**
A potential bug you could run into is if you haven't put a name attribute on the select tag
The name attribute is what the server sees. In the search method in listings/views.py, and you're looking at the request.GET['bedrooms'], this is looking at the form field that has the name of bedrooms. So, if you don't have the name attribute, the server won't know what you're talking about.
In sum, when you dealing with server side in the front end, the two most important attributes are (i) the name attribute and (ii) the action of the form tag (because that tells the server where to submit to)
<select class="form-control"> should be: <select name="state" class="form-control">

**Preserving Form Input for text fields**
The functionality that we want to include is that, when we search something (e.g. bedrooms or price), the search stays in the form once the server shows us the results
To do that, we will need to edit the search.html file & also the listings/views.py
The key step is adding 'values' to our context in listings/views.py. We pass in our whole GET Request into that variable called values

```py listings/views.py
context = {
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'state_choices': state_choices,
    'listings': queryset_list,
    # Add 'values' as a key and the whole get request is the value. That will mean that the whole get request will be available for us to use in the html template
    # As an example, if we search for search?keywords=pool&city= then request.get.keywords will be available to us as values.keywords
    'values': request.GET
}
```

Once we've done that, we can add in a value attribute in the templates/listings/search.html
This now means that the word we searched for will still be there after we have searched for it (i.e. the form input is preserved)
For text fields such as keywords and city, this is easy because we can simply put a value

Previous:
<input type="text" name="keywords" class="form-control" placeholder="Keyword (Pool, Garage, etc)">
Now:
<input type="text" name="keywords" class="form-control" placeholder="Keyword (Pool, Garage, etc)" value="{{ values.keywords }}">
<input type="text" name="city" class="form-control" placeholder="City"  value="{{ values.city }}">

**Preserving Form Input for Select Lists**
For <select> lists, it is different. You need conditionals.
The way we make an option selected is by adding 'selected' to the option tag. We need to loop through the dictionary of choices and determine which one should be selected

Make sure you do this for all the selects
```html templates/listings/search.html
{% if state_choices %}
    {% for key, value in state_choices.items %}
        <!-- If the key is equal to value.state, then we want to add 'selected' as an attribute -->    
        <option value="{{ key }}"                            
            {% if key == values.state %}
                selected
            {% endif %}
        >{{ value }}</option>
    {% endfor %}
{% endif %}
```

===**Authentication**===
Most applications that you will build will have front facing user accounts. We want users to be able to register from the front end & log in.
If we only had it that the admins were the only ones who had log in privileges, then we wouldn't get the full view of Django
The first step for Authentication is to create a new app called accounts

01 $ source ./venv/Scripts/activate && pip freeze
02 $ python manage.py startapp accounts
03 In btre/settings.py add the new app `INSTALLED_APPS = [ 'accounts.apps.AccountsConfig', ... ]`

Django already has a user system in place. This means that we don't have to create an account or user model. We can just use the user table that is already in place
You can see the tables in pgAdmin => Database => Schemas=> Tables => AuthUser
The columns include username, firstname, lastname, is_staff (which allows them to log in to the backend etc.)

04 Create routes for register and login `$ touch accounts/urls.py`
05 `path('accounts/', include('accounts.urls')),`
06 Create methods in accounts/views.py
07 $ mkdir templates/accounts && touch templates/accounts/register.html templates/accounts/login.html templates/accounts/dashboard.html
08 Test the routes: http://localhost:8000/accounts/dasboard, http://localhost:8000/accounts/register, http://localhost:8000/accounts/login, http://localhost:8000/accounts/logout

```py btre/settings.py
INSTALLED_APPS = [
    # This is a key step and a step that is easy to forget about
    ...
    'accounts.apps.AccountsConfig',
    ...
]
```

```py accounts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register')
]
```

```py accounts/views.py
from django.shortcuts import render, redirect

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):
    return render(request, 'accounts/register.html')
```

```py btre/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    # Bring accounts into the main urls.py. This means that anything with accounts slash, we will include the accounts urls
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Logout with redirect**
Note that the logic for logout is different as we don't want to render a template when the user logs out. Instead, we want to redirect the user to the index.
The redirect method takes one argument: the url you want to be redirect to as a string.

```py accounts/views.py
def logout(request):
    return redirect('index')
```

**Debugging with HttpResponse**
If you get any issues with the routes, one way to debug is to import HttpResponse & see if that works

```py accounts/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Success with HttpResponse I</h1>')
```

**Updating the HTML for the dashboard, login and register templates**
01 Bring in the static html for dashboard, login and register from the bootstrap-theme folder
02 {% extends 'base.html' %} on all three
03 Remove unnecessary static code on all three
04 Wrap text in {% block content %} and {% endblock %} on all three
05 Change static links on templates/partials/_navbar <a class="nav-link" href="register.html"> to <a class="nav-link" href="{% url 'register' %}">

**Conditionals for Highlighting Links**
Once the user is logged in, they are not going to want to see Register and Login on the navbar
Therefore, we should include conditionals that will have a message "Welcome, Username" and then there will be a link to the dashboard

This is done (as above) by editing the opening <li> tag

After a conditional, it looks like this:
```html templates/partials/_navbar.html
<li
{% if 'login' in request.path %}
    class="nav-item active mr-3"
{% else %}
    class="nav-item mr-3"
{% endif %}
>
<a class="nav-link" href="{% url 'login' %}">
        <i class="fas fa-sign-in-alt"></i>Login</a>
</li>
```

**i**
Change action on the form tag in register.html. Currently it is <form action="index.html">
By default, it will do a GET Request. You want to specify a POST Request

Very important to remember when you have a form an you are making a POST Request, you want to add a CRSF Token, which prevents cross site forgery. It ties your form to the current session so that no forgery can take place.
Within Django, it is easy to implement

```html register.html
<form action="{% url 'register' %}" method="POST">

```

**Cross-Site Request Forgery (CRSF) Tokens**

# (CSRF) in simple words
[Scenario without CRSF Tokens](https://stackoverflow.com/questions/5207160/what-is-a-csrf-token-what-is-its-importance-and-how-does-it-work)
Assume you are currently logged into your online banking at www.mybank.com
Assume a money transfer from mybank.com will result in a request of (conceptually) the form http://www.mybank.com/transfer?to=<SomeAccountnumber>;amount=<SomeAmount>. (Your account number is not needed, because it is implied by your login.)
You visit www.cute-cat-pictures.org, not knowing that it is a malicious site.
If the owner of that site knows the form of the above request (easy!) and correctly guesses you are logged into mybank.com (requires some luck!), they could include on their page a request like http://www.mybank.com/transfer?to=123456;amount=10000 (where 123456 is the number of their Cayman Islands account and 10000 is an amount that you previously thought you were glad to possess).
You retrieved that www.cute-cat-pictures.org page, so your browser will make that request
Your bank cannot recognize this origin of the request: Your web browser will send the request along with your www.mybank.com cookie and it will look perfectly legitimate. There goes your money!
This is the world without CSRF tokens.

*Scenario with CRSF Tokens*
The transfer request is extended with a third argument: http://www.mybank.com/transfer?to=123456;amount=10000;token=31415926535897932384626433832795028841971.
That token is a huge, impossible-to-guess random number that mybank.com will include on their own web page when they serve it to you. It is different each time they serve any page to anybody.
The attacker is not able to guess the token, is not able to convince your web browser to surrender it (if the browser works correctly...), and so the attacker will not be able to create a valid request, because requests with the wrong token (or no token) will be refused by www.mybank.com.

It would be worthy to note that script from www.cute-cat-pictures.org normally does not have access to your anti-CSRF token from www.mybank.com because of HTTP access control. This note is important for some people who unreasonably send a header Access-Control-Allow-Origin: * for every website response without knowing what it is for, just because they can't use the API from another website.

**i**
CSRF Middleware is activated by default in the MIDDLEWARE setting in settings.py `django.middleware.csrf.CsrfViewMiddleware`
To include it, you add e.g. <form method="post">{% csrf_token %}

You can look at this by Inspecting the form on Chrome (Ctrl + Shift + I)
<form action="/accounts/register" method="POST">
<input type="hidden" name="csrfmiddlewaretoken" value="82r3R30CZoaYgM5Llx8nCDRsxE7xncKbQhPdr4vaQStyeISphJbQ0yZHHCr9FcGF">

**o**
When the requests get submitted, we need to identify if we are seeing a GET or POST request. Therefore, we should include the logic below on both the login and register methods

```py accounts/views.py
def login(request):
    # If it's equal to post, we know that it's the form submission
    if request.method == 'POST':
        # Test by completing the form and submitting a registered user
        print('POST: placeholder text until logic is in place')
        return redirect('register')
    else:
        return render(request, 'accounts/login.html')
```

**Add logic to register the user**
We are going to add logic to register the user
We are also going to do some client side validation (built in HTML5 / JavaScript stuff)
On the server side, we need to make sure that the passwords match. We also need to check that there isn't an email or username that has already been used.
We also want to have an alert message that tells you "success, you are logged in"

**Django's Messages App**
Configure Flash Messages / Bootstrap Alerts
Django comes with a messages app ('django.contrib.messages')
It is in INSTALLED_APPS in settings.py
https://docs.djangoproject.com/en/3.0/ref/contrib/messages/

**Messages Levels**
There are five built-in levels of messages
Debug => Dev related messages that will be ignored in Prod
Info => Informational messages for the user
Success => Action was successful (e.g. "Your profile was updated successfully"
Warning => An error did not occur but it may be imminent
Error => An action was not successful or some other failure occurred

**Add message tags to settings.py**
Adding message tags into our settings file

```py settings.py
# Messages
# https://docs.djangoproject.com/en/3.0/ref/contrib/messages/
# Traversy gets rid of '50: 'critical' and messages.INFO: ''
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
```

**_alerts Partial**
$ touch templates/partials/_alerts.html
We are going to use Bootstrap markup within _alerts.html
We want to see if there is a message

```html templates/partials/_alerts.html
{% if messages %}
    <!-- If there are messages, we want to loop through them -->
    {% for single_message in messages %}
        <!-- Put in Bootstrap Markup -->
        <div id="message" class="container">
            <!-- In settings.py, we wrote messages.ERROR: 'danger', therefore we replace alert-danger with alert-{{ message.tags }}-->
            <!-- We also want to user to be able to dismiss this (close with x), so we add the tag alert-dismissible -->
            <!-- <div class="alert alert-danger"> -->
            <div class="alert alert-{{ single_message.tags }} alert-dismissible text-center" role="alert">
                <!-- As it is a dismissible alert, we need a button -->
                <!-- data-dismiss is a Bootstrap attribute -->
                <!-- The entity &times; gives it an 'x' -->
                <!-- https://getbootstrap.com/docs/4.3/components/alerts/ -->
                <button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span></button>
                <strong>
                    {% if single_message.level == DEFAULT_MESSAGE_LEVELS.ERROR %}
                        Error:
                    {% else %}
                        {{ messages.tags | title }}
                    {% endif %}
                </strong>
                    <!-- Then we display the message -->
                    {{ single_message }}
            </div>
        </div>
    {% endfor %}

{% endif %}
```

**Testing Registration**
To test, we need to add a redirect to views.py
We want to output the partial _alerts.html wherever we want errors to be able to go

```py accounts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
...
def register(request):
    if request.method == 'POST':
        # To use messages, we need to bring it in at the top `from django.contrib import messages`
        # To test, we are going to output the message when we submit the form
        # We have to output the partial wherever we want errors to be able to go
        
        # To output the message, we pass in the request and whatever the error message is
        messages.error(request, 'Testing Error Msg')
        
        # Then redirect to the same page
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')
```

You then want to insert the partial into the register.html and login.html pages {% include 'partials/_alerts.html' %}

```html templates/accounts/register.html
<div class="card-body">
    <!-- Bring in the partial for alerts -->
    {% include 'partials/_alerts.html' %}
```

You can then test by inserting dummy data into http://localhost:8000/accounts/register. The message error should now appear

**Adding custom JavaScript for fadeOut**
You can add custom JavaScript if you want the message to disappear automatically.
btre/static/js/main.js

```js
// Use JQuery to do a fadeout
// setTimeout is a JS function that holds off from doing something, and then does something
// setTimeout takes in a function
// We want jQuery to grab the element with the id of message
// We want to do a slow fade-out
// The second paramater for setTimeout is the time (in milliseconds). We put 3000
setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);
```

Since we put the function in the static folder in btre, we need to run the command `collectstatic` so that it goes into the main static folder
$ source ./venv/Scripts/activate && pip freeze
$ python manage.py collectstatic
$ yes `to accept overwriting`

You can now check and the script should be in static/js/main.js
To test, you will probably need to restart the server
If you still get issues, you can reload the current page ignoring cached content (Ctrl + Shift + R on Chrome)

**Logic for Register Method**
We are going to cover the whole user registration; do some validation and register a user
Right now the logic we have in place is to check if the request is a POST request
Every form field that is submitted, we want to put into a variable

If they do match, we move on but we have more validation to do. We don't want duplicate emails and we don't want duplicate usernames
To check username, we need to bring in the username model (which comes as a default with Django) from django.contrib.auth.models import User
The objects method fetches from the database. We want to put a filter by username=username, which means that we are checking the username field in the database for this value in the variable we declared above
Add .exists method(). This method lets us know if that username exists

```py accounts/views.py
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

        else:
            messages.error(request, 'Passwords do not match')
            # Redirect to same page
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')
```

We now want to test by trying to register with the only user that is already set up on the database (check pgAdmin for the details). Note, you haven't actually added the logic to create the user in the database yet so you will only be able to test with that one account

**Options after user has been created**
There are two options for when you create the user
(1) User can be automatically logged in as soon as they have registered
(2) Redirect user to login form so they fill out their own credentials

```py accounts/views.py
...
else:
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
...
```

**viewing user on PgAdmin**
On PgAdmin, you can see that the user doesn't have staff_status & their password is hashed
With Django, you do not need to worry about the hashing of passwords. It happens automatically

**Add Ability for Messages on Homepage**
Add the ability to have messages appear on the homepage
You do this as before by including the partial in templates/pages/index.html
Because the partial has a class of container, it means that it will be put in the middle
{% include 'partials/_alerts.html' %}

**Logic for login method in views.py**
01 Take the names of the fields from templates/accounts/login.html
02 Create variables and assign them to the inputs
03 User authenticate method to autenticate user
04 If user is not None, user has been found so return success message and redirect to dashboard
05 Else, return error message & redirect to login

```py accounts/views.py
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
```

**is_staff**
https://docs.djangoproject.com/en/3.0/ref/contrib/auth/
Important to note: We can now register new users in the front end. Once we register a new user, though, we will be booted our of the backend (/admin) as the test users will not have is_staff attribute (boolean) to access the admin side

**Add dashboard and logout link to Navbar**
We already have the static html in the dashboard template, so let's now change the markup for the breadcrumb
When we've logged in, we don't want Register or Log In to show in the navbar so we need to add a conditional to the _navbar partials {% if user.is_authenticated %}
In the else, you want to show the login and register
Now create a dashboard link and logout link. First start with the dashboard by adding a <li> for the Dashboard link. Put the welcome message. Remember that we have access to the user object within all our templates. As we have access to the user object, it means that we can access any field of that object

```html templates/accounts/dashboard.html
<!-- <a href="index.html"> -->
<a href="{% url 'index' %}">
```

```html templates/partials/_navbar.html
{% if user.is_authenticated %}
<li
    {% if 'dashboard' in request.path %}
        class="nav-item active mr-3"
    {% else %}
        class="nav-item mr-3"
    {% endif %}
>
    <a class="nav-link" href="{% url 'dashboard' %}">Welcome, {{ user.username }} (Dashboard)</a>
</li>
...
```

**Log Out Functionality**
The logout can't be just a GET Request. It needs to be a POST Request. We therefore need to create a form that will look like a link. A form is what we use to make a post request
We could use JavaScript & the fetch API or AJAX, but we're going to do the form instead as it's more straightforward & has the same result

```html templates/partials/_navbar.html                    
<li class="nav-item mr-3">
    <!--    
        For the href of the Logout a tag, we want some JavaScript 
        When we click the link, the JavaScript will be run: JavaScript will look for the id of 'logout' and it will submit the form
    -->
    <a href="javascript:{document.getElementById('logout').submit}}" class="nav-link">
        <!-- Logout icon from font-awesome https://fontawesome.com/v4.7.0/icon/sign-out -->
        <i class="fas fa-sign-out-alt"></i>Logout
    </a>
    <!--    
        Create the form which takes user to the already create route of logout
        This will need a CRSF token
    -->
    <form action="{% url 'logout' %}" method="POST" id="logout">
        {% csrf_token %}
        <input type="hidden">
    </form>
</li>
```

```accounts/views.py
    ???
    ???
    ???
```

**Reminder to include the partial _alerts.html**
Remember to check that you included the partial _alerts ({% include 'partials/_alerts.html' %}) to dashboard, navbar & index

**Dynamic Page Titles**
We now want to change the titles for each page. We don't want them to have BT Real Estate on all of them
We want the titles of the listings by going into templates/base.html
It's standard practice to use a pipe character and to place that pipe character within the template
You should place a block title inside base.html & then go into each html template to load the block title
Within each template, you should put the title right about the content and the pipe character | should go between the {% block title %} and {% endblock %}

```html templates/base.html
<title>Traversy Real Estate {% block title %} {% endblock %} </title>
```

```html templates/pages/index.html
{% load humanize %}

{% block title %} | Welcome {% endblock %}

{% block content %}

```

```html templates/pages/listing.html
{% load humanize %}

{% block title %} | {{ one_listing }} {% endblock %}

{% block content %}
```

**Create contacts app with startapp**
Moving onto the contacts, we want to create a contacts app
$ source ./venv/Scripts/activate && pip freeze && python manage.py startapp contacts

01 Create contacts app with startapp
02 Create contacts model https://docs.djangoproject.com/en/3.0/topics/db/models/ in contacts/models.py
03 Once you define your model, tell Django that you are going to use the model by going to settings.py & including the model name in INSTALLED_APPS
04 Make the migrations: $ python manage.py makemigrations contacts (This step makes the migration file, but it doesn't actually run the migration)
05 Migration (and make the database table): % python manage.py migrate
06 You can test by going to pgAdmin UI or the psql shell

```py contacts/models.py
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
```

```py settings.py
INSTALLED_APPS = [
    #...
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
    #...
]
```

**Confusion with singular or plural**
Singular or Plural?
The apps tend to be plural (contacts app)
The model is always singular, with an uppercase first letter (class Contact(models.Model))

**Register contact model**
Register contact model in contacts/admin.py so that we can see the contacts in the admin area
Note: the term 'contacts' is confusing here. What is means is contact form submissions rather than people you know.

```py admin/admin.py
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
```

You can test to see if this is appearing in the admin part of the site by going to http://localhost:8000/admin/
You can add a contact, but it doesn't really make much sense why you would as it is supposed to be the users that send the contacts to you. Nonetheless, it is worthwhile adding a contact just to show that the model has been set up correctly.
One example when you might actually want to set up the contact yourself from the backend would be if someone from the company talked to someone outside of the website and they wanted to add their information into the admin area

**Prepare the Inquiry Form**
We now want to prepare the inquiry form
Change the hardcoded address
Make it so that if the user is logged in, the forms are automatically populated (the name and email forms)

01 Change value of property within inquiry form (templates/listings.html)
    from:
    <input type="text" name="listing" class="form-control" value="45 Drivewood Cirlce" disabled>
    to:
    <input type="text" name="listing" class="form-control" value="{{ one_listing.title }}" disabled>
02 Add POST method to form & send user to url ('contact') that we will create in a bit
    <form action="{% url 'contact' %}" method="POST">
03 As with all post forms in Django, we want to secure it with our CSRF (Cross-Site Request Forgery) token {% csrf_token %}
04 Create hidden field to send user ID to the server
05 Create another hidden field to send the realtor's email to the server so that an auto email can be generated to that realtor
    *As we have a relationship between the realtor and the listing, we can get any field from the Realtor model*
    <input type="hidden" name="realtor_email" value="{{ listing.realtor.email }}">
06 You also want to send over the listing ID
    <input type="hidden" name="listing_id" value="{{ listing.id }}">
07 Auto-populate name and email if the user is logged in 
    {% if user.is_authenticated %}
    https://docs.djangoproject.com/en/3.0/topics/auth/default/
08 Change listings/views.py to create logic for managing the POST Request
    $ touch contacts/urls.py
09 Create route in contacts/urls.py
10 Include the new route in the main urls.py (common mistake to leave this out)
11 Add the contact method in contacts/views.py
12 Note, when you test you will now see the name & the email on the inquiry form. When you click submit, however, you will get an error as the contact url doesn't have a template yet

```html templates/listing.html
<form action="{% url 'contact' %}" method="POST">
    {% csrf_token %}

    {% if user.is_authenticated %}
        <input type="hidden" name="user_id" value="{{ user.id }}">
        <!-- If the user is not authenticated, we still want to send the input but we want to send a value of 0. This makes things easier for us on the other side when we handle the submission -->
    {% else %}
        <input type="hidden" name="user_id" value="0">
    {% endif %}
        <input type="hidden" name="realtor_email" value="{{ listing.realtor.email }}">
        <input type="hidden" name="listing_id" value="{{ listing.id }}">
    <div class="form-group">
        <label for="property_name" class="col-form-label">Property:</label>
        <input type="text" name="listing" class="form-control" value="{{ one_listing.title }}" disabled>
    </div>
```

```py contacts/urls.py
# We only need one url in this file, and that's for the submission
from django.urls import path

from . import views

urlpatterns = [
    path('contact', views.contact, name='contact')
]
```

```py contacts/views.py
from django.shortcuts import render

# Create your views here.
def contact(request):
    return
```

```py urls.py
urlpatterns = [
    #...
    path('contacts/', include('contacts.urls')),
    #...
]
```

**Hidden Input Field**
The <input type="hidden"> defines a hidden input field.
[W3Schools](https://www.w3schools.com/tags/att_input_type_hidden.asp)
A hidden field lets web developers include data that cannot be seen or modified by users when a form is submitted. A hidden field often stores what database record that needs to be updated when the form is submitted.
Note: While the value is not displayed to the user in the page's content, it is visible (and can be edited) using any browser's developer tools or "View Source" functionality. Do not use hidden inputs as a form of security!

**Handle Submission of Contact Form**
01 Check whether it is a POST request in the contact method in contacts/views.py
02 Capture the form fields
03 Bring in the contact model `from .models import Contact` and messages `from django.contrib import messages`
04 Create an object called contact
05 Save the contact object
06 Return a success message
07 Redirect the user 
08 Add the alerts partial to the listings template

```py contacts/views.py
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
```

```html templates/listing.html
...
<!-- Include Alerts -->
{% include 'partials/_alerts.html' %}
...
```

### Check if User has already made an inquiry
*include text here*

```py contacts/views.py
# Check if user has already had an inquiry on this property
if request.user.is_authenticated:
    # If the user is logged in, then grab their id from the request (this is an hidden input on the form)
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

    else:
        contact = Contact(user_id=user_id, listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message)

        contact.save()

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)
```

You could also prevent non-logged in users from making an inquiry into the same property by using IP tracking, but that's out of scope of this course 

## Sending Emails with Django
[Django Email Documentation](https://docs.djangoproject.com/en/3.0/topics/email/)
Although Python provides a mail sending interface via the smtplib module, Django provides a couple of light wrappers over it. These wrappers are provided to make sending email extra quick, to help test email sending during development, and to provide support for platforms that can’t use SMTP.
The code lives in the django.core.mail module.

##### Syntax
```py
send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```

### Instructions
01 Bring in send mail `from django.core.mail import send_mail`
02 Add settings in settings.py

```py settings.py
# Email config (smtp = simple mail transfer protocol)
EMAIL_HOST = 'smtp.gmail.com'
# Gmail SMTP port (TLS): 587
# Gmail SMTP port (SSL): 465
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ralphpaynecode@gmail.com'
EMAIL_HOST_PASSWORD = '******'
EMAIL_USE_TLS = True
```

```py contacts/views.py
from django.core.mail import send_mail
#...
def contact(request):
#...
contact.save()

# We only want the email actually sent out if the contact has been saved
send_mail(
    'Property Listing Inquiry + listing', # Subject
    'There has been an inquiry for + listing. Sign into the admin panel for more info', # Body of message
    'ralphpaynecode@gmail.com', # from@example.com (Here you use the EMAIL_HOST_USER you specified in settings.py)
    [realtor_email, 'ralphpayne@gmail.com'], # ['to@example.com'] List of email addresses
    fail_silently=False # This means it will show us some error messages if something goes wrong
)

messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
return redirect('/listings/'+listing_id)
```

#### DateTime Errors
You might get an error with datetime. Have a look at the link below & switch to timezone
[RuntimeWarning: DateTimeField received a naive datetime](https://stackoverflow.com/questions/18622007/runtimewarning-datetimefield-received-a-naive-datetime)

TL;DR: If you get an error, use timezone.now() instead of datetime.datetime.now(). Don't forget to import timezone in the beginning of the file

#### Errors with Email
Setting up email is tricky. I used a gmail account and ran into the problem that Google requires users to enable "Less secured apps access" on settings so we can send email

Make sure you have done the following
- EMAIL_PORT should equal 587 in settings.py
- You need to switch "Allow less secure apps: ON. [Link]https://myaccount.google.com/lesssecureapps
- You might also need to unlock captcha in your google account from which you wish to send emails. Search for google display unlock captcha and open the first link that appears. Then press the continue button.

*Note: you need to hide your password. It is currently EMAIL_HOST_PASSWORD = '******'

### Making the Dashboard Dynamic
1. In views.py we want reach in to the database and get the contacts/inqueries for a certain user; we can do this with request.user
2. Bring in the Contact model `from contacts.models import Contact`
3. Order `order_by('-contact_date')` the fetched contacts & filter `filter(user_id=user_id)` them by user_id
4. In dashboard.html, make the name dynamic `<h2>Welcome {{user.first_name}} </h2>`
5. Create if statement `{% if contacts %}`
6. Wrap the inquiries in a for loop `{% for one_contact in contacts %}`
7. Make the href dynamic `href="{% url 'listing' one_contact.listing_id %}"`

Note, with the user object, you don't need to pass it in through views. With Django, you can use that object anywhere.

```html templates/dashboard.html
...
        {% for one_contact in contacts %}
            <tr>
                <td> {{ one_contact.id }} </td>
                <td> {{ one_contact.listing }} </td>
                <td>
                <a class="btn btn-light" href="{% url 'listing' one_contact.listing_id %}">View Listing</a>
                </td>
            </tr>
        {% endfor %}

        </tbody>
    </table>
{% else %}
    <p>You have not made any inquiries</p> 
{% endif %}
```

```py contacts/views.py
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
```

# Uploading to Digital Ocean
Go to the DevOps crib to see the walkthrough for deploying to Digital Ocean