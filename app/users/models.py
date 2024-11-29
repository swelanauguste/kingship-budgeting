from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ("customer", "Customer"),
        ("support", "Support Agent"),
        ("admin", "System Administrator"),
    )
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default="customer")
    phone = models.CharField(max_length=7, null=True, blank=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.email
