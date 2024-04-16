from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
	text = models.CharField(max_length=200) # a topic
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.text # return a string

class Entry(models.Model):
	# specific thing about a topic
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		# return a string
		return f"{self.text[:50]}..." # 50 characters of text