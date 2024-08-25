from django.shortcuts import render

def dashboard(request):
    return render(request, 'playmakersapp/index.html')

def events_management(request):
    pending_events = [
        {
            'title': 'CITC Intramurals',
            'organizer': 'John Doe',
            'email': 'johndoe@example.com',
            'department': 'CITC',
            'location': 'USTP Cafeteria',
            'genre': 'Pop rock',
            'start_date': 'June 06, 2024',
            'start_time': '10:00 AM',
            'end_date': 'June 06, 2024',
            'end_time': '5:00 PM'
        },
    ]

    past_events = [
        {
            'title': 'CITC Intramurals',
            'organizer': 'John Doe',
            'email': 'johndoe@example.com',
            'department': 'CITC',
            'location': 'USTP Cafeteria',
            'genre': 'Pop rock',
            'start_date': 'June 06, 2024',
            'start_time': '10:00 AM',
            'end_date': 'June 06, 2024',
            'end_time': '5:00 PM'
        },
    ]

    published_events = [
        {
            'title': 'CITC Intramurals',
            'organizer': 'John Doe',
            'email': 'johndoe@example.com',
            'department': 'CITC',
            'location': 'USTP Cafeteria',
            'genre': 'Pop rock',
            'start_date': 'June 06, 2024',
            'start_time': '10:00 AM',
            'end_date': 'June 06, 2024',
            'end_time': '5:00 PM',
            'participants': '5/5'
        },
    ]

    rejected_events = [
        {
            'title': 'CITC Intramurals',
            'organizer': 'John Doe',
            'email': 'johndoe@example.com',
            'department': 'CITC',
            'location': 'USTP Cafeteria',
            'genre': 'Pop rock',
            'start_date': 'June 06, 2024',
            'start_time': '10:00 AM',
            'end_date': 'June 06, 2024',
            'end_time': '5:00 PM'
        },
    ]

    approved_events = [
        {
            'title': 'CITC Intramurals',
            'organizer': 'John Doe',
            'email': 'johndoe@example.com',
            'department': 'CITC',
            'location': 'USTP Cafeteria',
            'genre': 'Pop rock',
            'start_date': 'June 06, 2024',
            'start_time': '10:00 AM',
            'end_date': 'June 06, 2024',
            'end_time': '5:00 PM'
        },
    ]

    ongoing_events = [
        {
            'title': 'CITC Intramurals',
            'organizer': 'John Doe',
            'email': 'johndoe@example.com',
            'department': 'CITC',
            'location': 'USTP Cafeteria',
            'genre': 'Pop rock',
            'start_date': 'June 06, 2024',
            'start_time': '10:00 AM',
            'end_date': 'June 06, 2024',
            'end_time': '5:00 PM',
            'participants': '0/10'
        },
        
    ]

    context = {
        'pending_events': pending_events,
        'past_events': past_events,
        'published_events': published_events,
        'rejected_events': rejected_events,
        'approved_events': approved_events,
        'ongoing_events': ongoing_events
    }

    return render(request, 'playmakersapp/event_management/events_management.html', context)

def member_organization(request):
    members = [
        {
            'id': 1,
            'name': 'Jie Clark Terec',
            'email': 'johndoe@ustp.edu.ph',
            'role': 'Percussionist, Keyboardist',
            'genre': 'Rock, Jazz',
            'mobile_no': '09161531814',
            'total_events_participated': 32,
            'join_date': '07-13-2020',
            'image_url': 'https://i.ibb.co/4KZnDYS/PLAYMAKERS-Logo.png',
        },
        # Add more members here...
    ]
    return render(request, 'playmakersapp/member_org/member_org.html', {'members': members})

def event_statistics(request):
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
                "backgroundColor": ["#4A148C", "#D6F8D6", "#FF9800"],
            }
        ],
    }

    context = {
        'event_distribution_data': event_distribution_data,
        'event_statistics_data': event_statistics_data,
    }

    return render(request, 'playmakersapp/event_stat/event_statistics.html', context)

def messages(request):
    return render(request, 'playmakersapp/messages.html')

def logout(request):
    return render(request, 'playmakersapp/logout.html')
