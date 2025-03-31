# admin.py
from django.contrib import admin
from .models import LostItem

class LostItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'contact_info', 'found_date', 'created_at')  # Now these fields are present in the model
    search_fields = ('name', 'location')  # Allows searching by these fields in the admin interface
    list_filter = ('found_date',)  # Adds filters to the admin panel
    ordering = ('-created_at',)  # Orders the list by creation date (most recent first)

admin.site.register(LostItem, LostItemAdmin)
