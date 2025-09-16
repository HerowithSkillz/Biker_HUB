from django.urls import path
from . import views
from .views import (
    BikeListView, BikeDetailView, BikeCreateView, BikeUpdateView,
    EventListView, EventDetailView, EventCreateView,
    EventUpdateView, EventDeleteView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    
    # Bike URLs
    path('bikes/', BikeListView.as_view(), name='bike-list'),
    path('bike/<int:pk>/', BikeDetailView.as_view(), name='bike-detail'),
    path('bike/new/', BikeCreateView.as_view(), name='bike-create'),
    path('bike/<int:pk>/update/', BikeUpdateView.as_view(), name='bike-update'),
    
    # Event URLs
    path('events/', EventListView.as_view(), name='event-list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('event/<int:pk>/join/', views.event_join, name='event-join'),
    path('event/<int:pk>/leave/', views.event_leave, name='event-leave'),
]