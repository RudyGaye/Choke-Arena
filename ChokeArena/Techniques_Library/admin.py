from django.contrib import admin
from .models import Technique, Category, Type, Position

@admin.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the Technique model.

    Displays selected fields in the admin list view, allows searching by name, description, category, type, and position,
    and enables filtering by category, type, and position.
    """
    list_display = ('name', 'category', 'type', 'position')  # Columns displayed in the list view
    search_fields = ('name', 'description', 'category__name', 'type__name', 'position__name')  # Fields searchable via the search box
    list_filter = ('category', 'type', 'position')  # Filters available on the right side of the list view

    # Additional customization options (e.g., readonly_fields, fieldsets) can be added here if needed.


# Registering additional models for management in the Django admin.
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Position)

