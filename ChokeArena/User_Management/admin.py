from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils import timezone
from datetime import timedelta
from User_Management.models import CustomUser

class RegistrationDateRangeFilter(SimpleListFilter):
    """
    Custom filter to filter users based on registration date range.
    """
    title = 'registration date'
    parameter_name = 'registration_date'

    def lookups(self, request, model_admin):
        return (
            ('last_30_days', 'Last 30 days'),
            ('this_year', 'This year'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'last_30_days':
            return queryset.filter(registration_date__gte=timezone.now() - timedelta(days=30))
        if self.value() == 'this_year':
            return queryset.filter(registration_date__year=timezone.now().year)
        return queryset

class UserAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the CustomUser model.
    This class customizes the admin interface for the CustomUser model,
    adding list display, search fields, list filters, and a custom password widget.
    """
    list_display = ('name', 'surname', 'email', 'level', 'registration_date', 'birth_date', 'get_age', 'sex')

    def get_age(self, obj):
        return obj.age
    get_age.admin_order_field = 'birth_date'  # Allows column sorting
    get_age.short_description = 'Age'
    
    search_fields = ('name', 'surname', 'email')
    list_filter = (RegistrationDateRangeFilter, 'level', 'sex')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is not None:
            form.base_fields.pop('password', None)
        return form

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    list_display = ('email', 'name', 'surname', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'surname', 'level', 'birth_date', 'sex')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'registration_date')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'surname', 'password1', 'password2'),
        }),
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    def has_change_permission(self, request, obj=None):
        # Ensure that only users with specific permissions can change user records
        if not request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)

admin.site.register(CustomUser, CustomUserAdmin)
