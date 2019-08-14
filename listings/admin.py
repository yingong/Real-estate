from django.contrib import admin
from .models import Listing
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'listDate',
                    'price', 'isPublished', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'isPublished')
    list_editable = ('isPublished',)


admin.site.register(Listing, ListingAdmin)
