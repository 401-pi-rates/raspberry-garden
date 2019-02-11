from django.db import models
from django.utils import timezone


class SoilMoisture(models.Model):
    """
    Model for the soil moisture data that comes from the RPi.
    """
    has_moisture = models.BooleanField()
    # time_stamp = models.DateTimeField(auto_now_add=True, blank=True)
    time_stamp = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return '{}'.format(self.time_stamp)

    def __str__(self):
        return '{}'.format(self.has_moisture)
