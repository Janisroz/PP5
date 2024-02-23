from django.shortcuts import render


# Create your views here.
def index(request):
    """
    Returns Index Page
    """
    return render(request, 'home/index.html')


def about_us(request):
    """
    Returns About us Page
    """
    return render(request, 'home/about-us.html')