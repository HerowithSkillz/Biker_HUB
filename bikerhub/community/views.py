from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Bike, Event, CommunityList, BikeImage
from django.urls import reverse_lazy
from .forms import EventForm, BikeForm
from django.http import HttpResponseRedirect
from django.contrib import messages

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
    form_class = BikeForm
    template_name = 'community/bike_form.html'
    success_url = reverse_lazy('bike-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BikeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bike
    form_class = BikeForm
    template_name = 'community/bike_form.html'
    success_url = reverse_lazy('bike-list')

    def test_func(self):
        bike = self.get_object()
        return self.request.user == bike.owner

    def form_valid(self, form):
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
    form_class = EventForm
    template_name = 'community/event_form.html'
    success_url = reverse_lazy('event-list')

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'community/event_form.html'
    success_url = reverse_lazy('event-list')

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.host

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'community/event_confirm_delete.html'
    success_url = reverse_lazy('event-list')

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.host

@login_required
def event_join(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user != event.host:  # Host can't join their own event
        event.participants.add(request.user)
        messages.success(request, 'You have successfully joined the event!')
    return HttpResponseRedirect(reverse_lazy('event-detail', kwargs={'pk': pk}))

@login_required
def event_leave(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user in event.participants.all():
        event.participants.remove(request.user)
        messages.success(request, 'You have left the event.')
    return HttpResponseRedirect(reverse_lazy('event-detail', kwargs={'pk': pk}))