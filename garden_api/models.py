from django.db import models


class SoilMoisture(models.Model):
    """
    """
    has_moisture = models.CharField(max_length=180)
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)


    def __repr__(self):
        return '{}'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)
