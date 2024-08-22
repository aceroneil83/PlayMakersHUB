from django.shortcuts import render

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
