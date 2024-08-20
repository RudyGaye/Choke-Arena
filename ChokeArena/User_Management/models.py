from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from Techniques_Library.models import Technique
from Training_Plans.models import TrainingPlan


class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser model.
    Handles the creation of regular users and superusers.
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
    
        if not extra_fields.get('name') or not extra_fields.get('surname'):
            raise ValueError('Name and surname must be set')
    
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        # Set default values for superuser-specific fields
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Ensure the superuser has the necessary permissions
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model extending Django's AbstractBaseUser and PermissionsMixin.
    Includes additional fields such as name, surname, level, birth date, and many-to-many relationships with Technique and TrainingPlan models.
    """

    # Choices for user levels (belts) and gender
    BELT_CHOICES = [
        ('White Belt', 'White Belt'),
        ('Blue Belt', 'Blue Belt'),
        ('Purple Belt', 'Purple Belt'),
        ('Brown Belt', 'Brown Belt'),
        ('Black Belt', 'Black Belt'),
    ]

    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    # User model fields
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Email must be unique for each user
    level = models.CharField(max_length=50, choices=BELT_CHOICES)
    registration_date = models.DateField(auto_now_add=True)  # Automatically set the field to now when the object is first created.
    birth_date = models.DateField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)

    # User status flags
    is_active = models.BooleanField(default=True)
    is_redactor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    # Many-to-many relationships
    library_techniques = models.ManyToManyField(Technique, related_name='user_library_techniques', blank=True)
    library_plans = models.ManyToManyField(TrainingPlan, related_name='user_library_plans', blank=True)

    # Manager for the model
    objects = CustomUserManager()

    # Define the unique identifier for the user model
    USERNAME_FIELD = 'email'
    
    # Required fields for creating a user (besides email and password)
    REQUIRED_FIELDS = ['name', 'surname', 'level', 'sex']

    @property
    def age(self):
        """
        Calculate the user's age based on the birth_date.
        """
        today = date.today()
        age = today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
        return age

    def save(self, *args, **kwargs):
        """
        Override the save method to include any custom save functionality.
        Currently, it just calls the superclass's save method.
        """
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of the user, typically the email.
        """
        return self.email
