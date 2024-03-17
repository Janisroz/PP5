from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.
def session_feed(request):
    """
    Display the session feed
    """
    form = PostForm
    sessions =  Post.objects.all()
    template = 'sessionfeed/sessionfeed.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
