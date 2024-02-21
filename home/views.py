from django.shortcuts import render


# Create your views here.
def index(request):
    """
    Returns Index Page
    """
    return render(request, 'home/index.html')
