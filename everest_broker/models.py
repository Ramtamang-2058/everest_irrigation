# everest_broker/models.py
from django.db import models

class ReceivedData(models.Model):
    data = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
