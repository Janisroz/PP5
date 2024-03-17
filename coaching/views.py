from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Session, Coach
# Create your views here.


def sessions(request):
    """ A view to show all products, including sorting and search queries """
    if not request.user.is_authenticated:
        messages.error(request, 'Please log in to view this page.')
        return redirect(reverse('account_login'))

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


def session_detail(request, session_id):
    """
    Returns a session detail page for each session
    """
    if not request.user.is_authenticated:
        messages.error(request, 'Please log in to view this page.')
        return redirect(reverse('account_login'))

    session = get_object_or_404(Session, pk=session_id)

    context = {
        'session' : session
    }

    return render(request, 'coaching/session_detail.html', context)