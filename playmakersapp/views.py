from django.shortcuts import render
from django.http import JsonResponse

def dashboard(request):
    return render(request, 'playmakersapp/index.html')

def events_management(request):
    return render(request, 'playmakersapp/event_management/events_management.html')

def member_organization(request):
    return render(request, 'playmakersapp/member_org/member_org.html')

def event_statistics(request):
    return render(request, 'playmakersapp/event_stat/event_statistics.html')

def messages(request):
    return render(request, 'playmakersapp/messages.html')

def help_support(request):
    return render(request, 'playmakersapp/help_support.html')

def profile(request):
    return render(request, 'playmakersapp/profile.html')

def settings(request):
    return render(request, 'playmakersapp/settings.html')

def logout(request):
    return render(request, 'playmakersapp/logout.html')


def event_statistics(request):
    # Example data for charts (replace with your actual data)
    event_distribution_data = {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "datasets": [
            {
                "label": "Events",
                "backgroundColor": "#4CAF50",
                "data": [10, 15, 23, 5, 9, 12, 13, 22, 19, 25, 17, 8],
            }
        ],
    }

    event_statistics_data = {
        "labels": ["Playmakers Events", "Department Events", "Organization Events"],
        "datasets": [
            {
                "data": [53, 31, 16],
                "backgroundColor": ["#4A148C", "#4CAF50", "#FF9800"],
            }
        ],
    }

    context = {
        'event_distribution_data': event_distribution_data,
        'event_statistics_data': event_statistics_data,
    }
    
    return render(request, 'playmakersapp/event_stat/event_statistics.html', context)