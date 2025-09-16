from django.urls import path
from . import views
from .views import BikeListView, BikeDetailView, BikeCreateView, EventListView, EventDetailView, EventCreateView

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('community/', views.community_list, name='community_list'),
    
    # Bike URLs
    path('bikes/', BikeListView.as_view(), name='bike-list'),
    path('bike/<int:pk>/', BikeDetailView.as_view(), name='bike-detail'),
    path('bike/new/', BikeCreateView.as_view(), name='bike-create'),
    
    # Event URLs
    path('events/', EventListView.as_view(), name='event-list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
]