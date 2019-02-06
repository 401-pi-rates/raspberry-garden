"""To control views of project django_lender."""
from django.db import models
from django.shortcuts import render
from garden_app.models import Temperature
from garden_api.models import SoilMoisture
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404


@login_required
def home_view(request):
    """To control views for the project django_lender."""
    water = SoilMoisture.objects.all().last()
    if water is 'True':
        read = 'Has Water'
    else:
        read = 'Dry'

    context = {
        'temperature': get_list_or_404(Temperature)[0],
        # 'waterlevel': get_list_or_404(SoilMoisture)[-1],
        'waterlevel': read,
    }
    return render(request, 'generic/home.html', context)
