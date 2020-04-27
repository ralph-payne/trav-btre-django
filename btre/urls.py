from django.contrib import admin
from django.urls import path, include
# We need to bring these two in for the media files to show up in the front end
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Leave path blank because we want the homepage to appear with nothing
    # include 'pages.urls' (note, you need to bring include in as part of the django.urls package)
    path('', include('pages.urls')),
    # Create listing. Anything that is listings slash is going to go to listings.urls (i.e. the # in the listings app)
    path('listings/', include('listings.urls')),
    # Create accounts
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    # If we don't include this setting, things won't show up correctly
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)