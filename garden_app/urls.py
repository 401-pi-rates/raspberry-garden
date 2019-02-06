"""To list any url paths."""
from django.urls import path
from .views import weekly_view, monthly_view


urlpatterns = [
    path('weekly', weekly_view, name='weekly'),
    path('monthly', monthly_view, name='monthly'),
]
