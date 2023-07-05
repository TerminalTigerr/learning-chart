from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """ The Home page for learning charts"""
    return render(request, 'learning_charts/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render (request, 'learning_charts/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all it's entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_charts/topic.html', context)

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data is submitted, create a blank form
        form = TopicForm()
    else:
        # Post data is submitted, process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_charts:topics')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_charts/new_topic.html', context)

def new_entry(request, topic_id):
    """Add a new entry for a partcular topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        # POST data submitted, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_charts:topic', topic_id=topic_id)
    # Display a blank or invalid form
    context = {'topic':topic, 'form': form}
    return render(request, 'learning_charts/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request, pre-fill form with the current entry
        form = EntryForm(instance=entry)
    else:
        # Post data submitted,process data
        form = EntryForm(instance=form, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_charts:topic', topic_id=topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_charts/edit_entry.html', context)