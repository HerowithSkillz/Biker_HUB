from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bike, Event, CommunityList
from django.urls import reverse_lazy

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def community_list(request):
    return render(request, 'community_list.html')

# Bike Views
class BikeListView(ListView):
    model = Bike
    template_name = 'community/bike_list.html'
    context_object_name = 'bikes'

class BikeDetailView(DetailView):
    model = Bike
    template_name = 'community/bike_detail.html'

class BikeCreateView(LoginRequiredMixin, CreateView):
    model = Bike
    template_name = 'community/bike_form.html'
    fields = ['name', 'brand', 'year', 'image', 'description']
    success_url = reverse_lazy('bike-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# Event Views
class EventListView(ListView):
    model = Event
    template_name = 'community/event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'community/event_detail.html'

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'community/event_form.html'
    fields = ['title', 'location', 'date', 'description']
    success_url = reverse_lazy('event-list')

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)