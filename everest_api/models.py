from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from django.utils import timezone

class CustomToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        expiration_time = self.created_at + timezone.timedelta(days=1)  # Set the desired expiration time
        return timezone.now() > expiration_time

