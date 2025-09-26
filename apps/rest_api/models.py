from django.db import models
from django.utils.crypto import get_random_string

class ApiKey(models.Model):
    key = models.CharField(max_length=40, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = get_random_string(length=40)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.key