"""To control views of project django_lender."""
from django.shortcuts import render
from garden_app.models import Temperature
from garden_api.models import SoilMoisture
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404


@login_required
def home_view(request):
    """To control views for the project django_lender."""

    # context = {
    #     'temperature': get_list_or_404(Temperature).filter(id=1),
        # 'waterlevel': get_list_or_404(SoilMoisture),
    # }

    # users = User.objects.annotate(max_trophy_info_id=Max('gameusertrophyinfo__id'))
    # ids = [user.max_trophy_info_id for user in users]
    # trophy_infos = gameUserTrophyInfo.objects.filter(id__in = ids)


    return render(request, 'generic/home.html', context)
