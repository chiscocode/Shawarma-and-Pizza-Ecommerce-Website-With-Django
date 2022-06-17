from django.contrib import admin
from .models import *

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
  list_display = ('name','email', 'phone', 'contact_date')
  list_display_links = ('name','phone', 'email')
  search_fields = ('name','email', 'phone')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)
