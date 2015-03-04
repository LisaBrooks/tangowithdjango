from django.db import models
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

class Game(models.Model):
	# each game requires a unique number to identify it. 
	number = models.IntegerField(default=0, unique=True)
	# current board status is also required here. 

	# this is used to create the URL of each game
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.number)
		super(Game, self).save(*args, **kwargs)

	# return the primary key of game - the session number	
	def __unichr__(self):
		return self.number	

class UProfile(models.Model):
	# Link the UProfile to the User model instance.
	user = models.OneToOneField(User)

	# User already comes with attributes - username and password 
	# Bao allows their users to upload a profile picture if they 
	# want to. As this is optional set blank to be True.
	# Users also have a score.
	picture = models.ImageField(upload_to='profile_images', blank = True)
	score = models.IntegerField(default=0, blank=True)

	# this class returns the user's username
	def __unicode__(self):
		return self.user.username
