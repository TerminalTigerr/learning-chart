from django.shortcuts import render
from .models import Topic

def index(request):
    """ The Home page for learning charts"""
    return render(request, 'learning_charts/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render (request, 'learning_charts/topics.html', context)
