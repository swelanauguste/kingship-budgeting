import uuid

from django.db import models
from django.utils.text import slugify
from users.models import User


class Account(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, null=True, unique=True, blank=True)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")

    class Meta:
        ordering = ["amount"]
        unique_together = ["name", "owner"]
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.uid, self.name)
        super(Account, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
