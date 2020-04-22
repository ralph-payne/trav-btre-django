from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Leave path blank because we want the homepage to appear with nothing
    # include 'pages.urls' (note, you need to bring include in as part of the django.urls package)
    path('', include('pages.urls')),
    # Create listing. Anything that is listings slash is going to go to listings.urls
    path('listing/', include('listings.urls')),
    path('admin/', admin.site.urls),
]