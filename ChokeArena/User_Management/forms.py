from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.core.validators import EmailValidator
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    """
    Form for creating a new user. Inherits from UserCreationForm.
    Includes fields for name, surname, email, level, birth date, and sex.
    Widgets are customized for better integration with Bootstrap.
    """
    
    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'email', 'level', 'birth_date', 'sex']
        
        # Customizing form widgets with Bootstrap classes
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-select'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sex': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_email(self):
        """
        Validate that the email is unique in the system.
        Raises a ValidationError if the email is already in use.
        """
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

class LoginForm(forms.Form):
    """
    Simple login form with fields for email and password.
    Custom widgets are applied for Bootstrap styling.
    """
    
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def confirm_login_allowed(self, user):
        """
        Confirm that the user is allowed to log in.
        """
        if not user.is_active:
            raise forms.ValidationError("This account is inactive.")

class CustomUserChangeForm(UserChangeForm):
    """
    Form for updating an existing user. Inherits from UserChangeForm.
    Includes fields for name, surname, level, birth date, sex, and password.
    Widgets are customized for better integration with Bootstrap.
    """
    password = ReadOnlyPasswordHashField(label="Password", help_text=(
        "Passwords are hashed in the database, so you cannot see this user's "
        "password, but you can change it using <a href=\"password/\">this form</a>."
    ))

    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'level', 'birth_date', 'sex', 'password']

        # Customizing form widgets with Bootstrap classes
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-select'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sex': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]