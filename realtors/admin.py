from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 25

# Register model
# def register(self, model_or_iterable, admin_class=None, **options):
admin.site.register(Realtor, RealtorAdmin)