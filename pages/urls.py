# If you want to define a path, you will actually have to bring the path package in
from django.urls import path

# Bring in the views because the idea is to have a path/url/route that is attached to a method inside the view file
from . import views # the 'from .' is saying 'from current folder'

urlpatterns = [
    # We can use path because we brought the path package in at the top of this code
    # The first parameter is '' (the route path / the homepage). In a lot of frameworks you will see '/', but we leave it empty in Django
    # The second parameter is the method we want to connect this to in the view (views.index)
    # The third and final parameter is the name. We set the name here to easily access the path, which we'll call 'index'
    path('', views.index, name='index'),
    
    # Create an about route, with the method name also about. We will get an error initially as there is no about method in the views file so we will have to create that in 
    path('about', views.about, name='about')
]

# If you haven't created the method called index or about, you will get an error in the console. You need to create these methods in the views folder