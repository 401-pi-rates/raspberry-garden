from .models import Temperature
from garden_api.models import SoilMoisture
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404


@login_required
def weekly_view(request):
    """To render weekly_view with its content."""
    context = {
        'temperatures': get_list_or_404(Temperature),
        'waterlevel': get_list_or_404(SoilMoisture),
    }

    # context = {
    #     'temperatures': [{'has_moisture': 'true', 'date': 'Feb 5'}]
    # }
    return render(request, 'raspberry/weekly.html', context)


@login_required
def monthly_view(request):
    """To render monthly_view with its content."""
    context = {
        'temperatures': get_list_or_404(Temperature)
    }

    return render(request, 'raspberry/monthly.html', context)
