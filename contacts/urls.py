# We only need one url in this file, and that's for the submission
from django.urls import path

from . import views

urlpatterns = [
    path('contact', views.contact, name='contact')
]