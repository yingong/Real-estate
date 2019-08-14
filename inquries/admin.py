from django.contrib import admin
from .models import Inquiry
# Register your models here.


class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'listing_id',
                    'user_id', 'name', 'Inquiry_date')
    list_display_links = ('user_id', 'listing_id')


admin.site.register(Inquiry, InquiryAdmin)
