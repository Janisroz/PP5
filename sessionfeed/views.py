from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.
def session_feed(request):
    """
    Display the session feed
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post succesfull')
            return redirect('session_feed')
        else:
            messages.error(request, 'Post failed. Please ensure the form is valid.')

    form = PostForm
    sessions =  Post.objects.all()
    template = 'sessionfeed/sessionfeed.html'

    context = {
        'form': form,
        'sessions':sessions
    }

    return render(request, template, context)
