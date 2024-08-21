from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(BaseUserAdmin):
    """
    Custom admin panel configuration for the CustomUser model.
    Uses CustomUserCreationForm for adding users and CustomUserChangeForm for editing users.
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('email', 'name', 'surname', 'level', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'level', 'sex', 'groups')
    search_fields = ('email', 'name', 'surname')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'surname', 'level', 'birth_date', 'sex')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_redactor', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('User Techniques and Plans'), {'fields': ('library_techniques', 'library_plans')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'surname', 'level', 'birth_date', 'sex', 'password1', 'password2', 'is_staff', 'is_active', 'groups'),
        }),
    )

    filter_horizontal = ('library_techniques', 'library_plans', 'groups', 'user_permissions')

admin.site.register(CustomUser, CustomUserAdmin)

# Optionally, you can also register the Group model if it's not already registered.
