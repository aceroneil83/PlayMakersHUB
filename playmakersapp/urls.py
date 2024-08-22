from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('events-management/', views.events_management, name='events_management'),
    path('member-organization/', views.member_organization, name='member_organization'),
    path('event-statistics/', views.event_statistics, name='event_statistics'),
    path('messages/', views.messages, name='messages'),
    path('help-support/', views.help_support, name='help_support'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout, name='logout'),
]
