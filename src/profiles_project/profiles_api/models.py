from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from . import managers

# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a 'user profile' inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = managers.UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get user full name."""
        return self.name

    def get_short_name(self):
        """Used to get user short name."""
        return self.name

    def __str__(self):
        return '{self.name} - {self.email}'

