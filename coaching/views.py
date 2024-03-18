from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Session, Coach
from .forms import CoachForm, SessionForm
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


def add_coach(request):
    """ Add a coach to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('coaching/all_coaches.html'))

    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES)
        if form.is_valid():
            coach = form.save()
            messages.success(request, 'Successfully added new coach!')
            return redirect(reverse('all_coaches'))
        else:
            messages.error(request, 'Failed to add coach. Please ensure the form is valid.')
    else:
        form = CoachForm()

    template = 'coaching/add_coach.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_coach(request, coach_id):
    """ Edit a coach """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('all_coaches'))

    coach = get_object_or_404(Coach, pk=coach_id)
    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES, instance=coach)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated coach!')
            return redirect(reverse('all_coaches'))
        else:
            messages.error(request, 'Failed to update coach. Please ensure the form is valid.')
    else:
        form = CoachForm(instance=coach)
        messages.info(request, f'You are editing {coach.name}')

    template = 'coaching/edit_coach.html'
    context = {
        'form': form,
        'coach': coach,
    }

    return render(request, template, context)


def delete_coach(request, coach_id):
    """ Delete a coach from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('all_coaches'))

    coach = get_object_or_404(Coach, pk=coach_id)
    coach.delete()
    messages.success(request, 'Coach deleted!')
    return redirect(reverse('all_coaches'))


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


def add_session(request):
    """
    Add a sesion to the site
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('coaching/all_sessions.html'))

    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            coach = form.save()
            messages.success(request, 'Successfully added new session!')
            return redirect(reverse('all_sessions'))
        else:
            messages.error(request, 'Failed to add session. Please ensure the form is valid.')
    else:
        form = SessionForm()

    template = 'coaching/add_session.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def delete_session(request, session_id):
    """ Delete a session from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('all_sessions'))

    session = get_object_or_404(Session, pk=session_id)
    session.delete()
    messages.success(request, 'Session deleted!')
    return redirect(reverse('all_sessions'))
