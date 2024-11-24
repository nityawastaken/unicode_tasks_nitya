# users/models.py

from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models

class User(AbstractUser):
    ROLES = [('user', 'User'), ('tour_guide', 'Tour Guide')]
    role = models.CharField(max_length=20, choices=ROLES)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['email']

    groups = models.ManyToManyField(
        Group,
        related_name='user_groups',  # Unique related name for groups
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permissions',  # Unique related name for permissions
        blank=True
    )

    def __str__(self):
        return self.username
