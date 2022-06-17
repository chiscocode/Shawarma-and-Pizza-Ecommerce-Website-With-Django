from django.contrib import admin

# Register your models here.
from .models import *
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'staff','title','price','stock',)
    list_filter = ("title",)
    prepopulated_fields={'slug': ('title',)}
    search_fields = ['title', 'price']

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
