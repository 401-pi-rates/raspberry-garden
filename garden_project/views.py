"""To control views of project django_lender."""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404


@login_required
def home_view(request):
    """To control views for the project django_lender."""
    return render(request, 'generic/home.html')
