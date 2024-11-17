from django.shortcuts import render
from .models import JlolData
from django.core.exceptions import ValidationError
from datetime import datetime
# Home Page View
def home_view(request):
    return render(request, 'jloldata/home.html')
def jloldata_view(request):
    # Filters and search
    joining_filter = request.GET.get('joining', '')
    role_filter = request.GET.get('role', '')
    search_query = request.GET.get('search', '')

    # Exclude specific usernames
    excluded_usernames = ['Esther David', 'Subhasree Dey', 'Parna Sarkar', 'Esther Shilpa', 'Antony Arockianathan', 'Karthika','Tinish']

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

    # Get unique values for dropdowns
    joining_options = JlolData.objects.values_list('joining', flat=True).distinct()
    role_options = JlolData.objects.values_list('role', flat=True).distinct()

    # Add 'joined' as a special option in the joining dropdown
    joining_options = ['joined'] + list(joining_options)

    # Handle OL Date update
    if request.method == 'POST':
        dt_ct_name = request.POST.get('dt_ct_name')
        ol_date = request.POST.get('ol_date')

        # Validate the date format
        try:
            # Try to convert the date to the correct format
            ol_date = datetime.strptime(ol_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValidationError("The OL Date must be in YYYY-MM-DD format.")

        # Update OL Date in the database
        if dt_ct_name and ol_date:
            entry = JlolData.objects.filter(dt_ct_name=dt_ct_name).first()
            if entry:
                entry.ol_date = ol_date
                entry.save()

    context = {
        'data': data,
        'joining_options': joining_options,
        'role_options': role_options,
    }

    return render(request, 'jloldata/jloldata.html', context)
