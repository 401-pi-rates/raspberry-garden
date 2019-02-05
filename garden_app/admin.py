"""To register model Temperature with admin."""
from django.contrib import admin
from .models import Temperature


admin.site.register((Temperature,))
