from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Registration
from django.contrib.auth.decorators import login_required

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        # Register only after confirmation
        Registration.objects.create(user=request.user, event=event)
        return redirect('my_registrations')

    # Show confirmation page first
    return render(request, 'events/register_event.html', {'event': event})


@login_required
def my_registrations(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'events/my_registrations.html', {'registrations': registrations})

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    print("Custom logout view called")  # This should show in terminal!
    logout(request)
    return redirect('login')
