from django.db import models

class Test(models.Model):
    """
    """
    has_moisture = models.CharField(max_length=180)

    def __repr__(self):
        return '{}'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)
