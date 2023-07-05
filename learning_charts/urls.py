"""Defining URL patterns for learning charts"""

from django.urls import path
from . import views

app_name = 'learning_charts'
urlpatterns = [
    # Home page 
    path('', views.index, name='index'),

    # Page showing all topics
    path('topics/', views.topics, name='topics'),
    # Detailed page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic')
]