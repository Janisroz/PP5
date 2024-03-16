from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Session, Coach
# Create your views here.

def sessions(request):
    """ A view to show all products, including sorting and search queries """

    all_sessions = Session.objects.all()

    context = {
        'all_sessions': all_sessions,
    }

    return render(request, 'coaching/all_sessions.html', context)
    

def coaches(request):
    """ A view to show all coaches """

    all_coaches = Coach.objects.all()

    context = {
        'all_coaches': all_coaches,
    }

    return render(request, 'coaching/all_coaches.html', context)