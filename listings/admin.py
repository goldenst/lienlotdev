from django.contrib import admin

# Register your models here.
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'is_published','year','make','model', 'price', 'seller')
  list_display_links = ('id', 'make')
  list_filter = ('seller',)
  list_editable = ('is_published',)
  search_fields = ('year', 'make', 'model',)
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)