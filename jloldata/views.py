from django.shortcuts import render
from .models import JlolData
from django.core.exceptions import ValidationError
from datetime import datetime
# Home Page View
def home_view(request):
    return render(request, 'jloldata/home.html')
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import JlolData

def jloldata_view(request):
    # Filters and search
    joining_filter = request.GET.get('joining', '')
    role_filter = request.GET.get('role', '')
    search_query = request.GET.get('search', '')

    # Exclude specific usernames
    excluded_usernames = ['Esther David', 'Subhasree Dey', 'Parna Sarkar', 'Esther Shilpa', 'Antony Arockianathan', 'Karthika']

    # Filter the data based on the request parameters
    data = JlolData.objects.all()

    # Exclude records with the specific usernames
    data = data.exclude(username__in=excluded_usernames)

    # Apply joining filter
    if joining_filter == 'joined':
        data = data.exclude(joining='not joined')
    elif joining_filter:
        data = data.filter(joining=joining_filter)

    # Apply role filter
    if role_filter:
        data = data.filter(role=role_filter)

    # Apply search query filter
    if search_query:
        data = data.filter(username__icontains=search_query)

    # Paginate data
    paginator = Paginator(data, 1500)  # Show 10 records per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Get unique values for dropdowns
    joining_options = JlolData.objects.values_list('joining', flat=True).distinct()
    role_options = JlolData.objects.values_list('role', flat=True).distinct()

    context = {
        'page_obj': page_obj,
        'joining_options': joining_options,
        'role_options': role_options,
    }

    return render(request, 'jloldata/jloldata.html', context)
