# defines URL patterns for learning_logs

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
	# home page
	path('', views.index, name='index'),
	# page allowing all topics
	path('topics/', views.topics, name='topics'),
	# detail page for a single topic
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	# page for adding new topic
	path('new_topic/', views.new_topic, name='new_topic'),
	# page for new entry
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	# page for editing an entry
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
