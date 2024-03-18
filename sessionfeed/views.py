from django.shortcuts import render, redirect, reverse, get_object_or_404
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


def delete_post(request, session_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('session_feed'))

    session = get_object_or_404(Post, pk=session_id)
    session.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('session_feed'))