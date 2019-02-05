"""To set up models for the gardens app."""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Temperature(models.Model):
    """To set up Temperature class."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='temperature')
    temperature = models.CharField(max_length=48)
    date_added = models.DateTimeField(default=timezone.now)

    # def __repr__(self):
    #     return ''

    def __str__(self):
        return f'{self.date_added} ({self.temperature})'


class WaterLevel(models.Model):
    """To set up WaterLevel class."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='waterlevel')
    water = models.CharField(max_length=48)
    date_added = models.DateTimeField(default=timezone.now)

    # def __repr__(self):
    #     return ''

    def __str__(self):
        return f'{self.date_added} ({self.water})'
