from django.shortcuts import render
from datetime import datetime  
from django.http import HttpResponseRedirect
from .models import Event, Venue     
from .forms import VenueForm    
from .forms import EventForm


# Create your views here.
def home(request):
    return render(request, 'events/home.html', {})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})

def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})
    

def search_events(request):
    if request.method == "POST":
        searched = request.POST['searched']
        events = Event.objects.filter(name__contains= searched)
        return render(request, 'events/search_events.html', {'searched': searched, 'events': events })
    else:
        return render(request, 'events/search_events.html',)



def events_list(request):
    event_list = Event.objects.all()
    return render(request, 'events/events_list.html', {'events_list': event_list})
