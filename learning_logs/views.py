from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Topic, Entry
from .forms import TopicForm, EntryForm 

from django.http import Http404 # error 404

# Create your views here.

def index(request):
	# home page for learning_log
	return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
	# show all topics
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
	# show a single topic and its entries
	topic = Topic.objects.get(id=topic_id)
	# make sure topic belongs to the current user
	if topic.owner != request.user:
		raise Http404

	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	# add new topic
	if request.method != 'POST':
		# no data, blank form
		form = TopicForm()
	else:
		form = TopicForm(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			#form.save()
			return redirect('learning_logs:topics')
	# display the blank/invalid topic
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	# new entry for topic
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		# balnk form
		form = EntryForm()
	else:
		# process data
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return redirect('learning_logs:topic', topic_id=topic_id)

	# display blank/invalid form
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	if request.method != 'POST':
		# initial request
		form = EntryForm(instance=entry)
	else:
		# process data
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topic', topic_id=topic.id)

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)
		#






""" ---- not needed ---- 
def register(request):
	# register a new user
	if request.method != 'POST':
		# display blank form
		form = UserCreationForm()
	else:
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# log in & redirect to home page
			login(request, new_user)
			return redirect('learning_logs:index')

	# display invalid form (blank)
	context = {'form': form}
	return render(request, 'registration/register.html', context)



"""





