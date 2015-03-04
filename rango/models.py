from django.db import models
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

#from admin import ModelAdmin
#from django.contrib import admin 


# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
			self.slug = slugify(self.name)
			super(Category, self).save(*args, **kwargs)

	def __unicode__(self): # this is for python 2, if i was working on python 3 : __str__
			return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __unicode__(self): # same as above __str__ if on P3
		return self.title	

class UserProfile(models.Model):
	# This line is required. Links UsereProfile to a User model instance.
	user = models.OneToOneField(User)

	# The additional attributes we wish to include
	# blank = True to allow either field to be left blank - users choice
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	# override the __unicode__() method to return out something meaningful
	def __unicode__(self):
		return self.user.username			
