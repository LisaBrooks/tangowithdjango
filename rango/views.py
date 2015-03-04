# -*- coding: utf-8 -*-

from django.shortcuts import render

# we first import HttpResponse object from the django.http module
from django.http import HttpResponseRedirect, HttpResponse

#import the category model
from rango.models import Category

# import the page model
from rango.models import Page

# import the category form, user form and user profile form 
from rango.forms import CategoryForm
from rango.forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate, login, logout

# this points the code to the @ before doing anything else.
# Checks if the user is logged in and then display correct info.
from django.contrib.auth.decorators import login_required

from datetime import datetime
# each view exists in this file as a series of individual functions 

# we have only created one view called index here.
def index(request):
	# each view returns a HttpResponse object. A simple one takes a 
	# String parameter representing the content of the page that we 
	# want to send to the client requesting the view.

	# also need to work in the url.py file to map a url to the view 

	# construct a dictionary to pass tp the template engine as its 
	# context. Note the key boldmessageis the same as {{ boldmessage }}
	# in the template!

	#context_dict = {'boldmessage': "I am bold font from the context"}

	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]
	context_dict = {'categories' : category_list, 'pages':page_list}

	# Get the number of visits to the site.
	# We use the COOKIES.get() function to obtain the visits cookie.
	# If the vookie exists, the value returned is casted to an integer.
	# If the cookie doesn't exist, we default to zero and cast that.
	
	#visits = int(request.COOKIES.get('visits', '1'))
	visits = request.session.get('visits')
	
	if not visits: 
		visits = 1	
	
	reset_last_visit_time = False

	last_visit = request.session.get('last_visit')
	if last_visit:
		last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# note that the first parameter is the template we wish to use.

	#response = render(request, 'rango/index.html', context_dict)

	# Does the cookie last_visit exist?
	#if 'last_visit' in request.COOKIES:
		#Yes it does! Get the cookie's value.
		#last_visit = request.COOKIES['last_visit']
		# Cast the value to a Python date/time object.
		#last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

		# If it's been more than a day since the last visit...
		if(datetime.now() - last_visit_time).seconds > 0:
			visits = visits + 1
			# and flag that the cookie last visit needs to be updated.
			reset_last_visit_time = True
	else: 
		# Cookie last visit doesn't exist, so flag that it shouldbe set.
		reset_last_visit_time = True

	if reset_last_visit_time:
		#response.set_cookie('last_visit', datetime.now())
		#response.set_cookie('visits', visits)
		request.session['last_visit'] = str(datetime.now())
		request.session['visits'] = visits
	context_dict['visits'] = visits
	
	#Obtain our Response object early so we can add cookie info
	response = render(request, 'rango/index.html', context_dict)	
	# return response back to the user, updating any cookies.
	return response		

def about(request):
	return render(request, 'rango/about.html')

	#return HttpResponse("Rango says here is the about page <br/> <a href=\"/rango/\">Back to main page</a>")	

def category(request, category_name_slug):
	# Create a context dictionary which we can pass to the template
	# rendering engine
	context_dict = {}

	try:
		# Can we find a category name slug with the given name?
		# If we can't, the .get() method raises a DoesNotExist exception
		# So the .get() method returns one model instance or raises an exception
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name

		# Retrieve all of the associated pages.
		# Note that filter returns >= 1 model instance.
		pages = Page.objects.filter(category=category)

		# Adds our results list to the template ontext under name pages
		context_dict['pages'] = pages

		# We also add the category object from the database to the context dictionary
		# We'll use this in the template to verify that the category exists

		context_dict['category'] = category

	except Category.DoesNotExist:
		# We get here if we didn't find the specified category.
		# Don't do anything - the template displays the "no category" message for us.
		pass

	# Go render the response and return it to the client
	return render(request, 'rango/category.html', context_dict)	

def add_category(request):
	# A HTTP POST?
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		#HAve we been provided with a valid form?
		if form.is_valid():
			# save the new category to the database
			form.save(commit=True)

			# Now call the index() view.
			# The user will be shown the homepage
			return index(request)
		else:
			# the supplied form contained errors therefore print them to the terminal
			print form.errors
	else:
		# If the request was not a POST, display the form to enter details.		
		form = CategoryForm()

		# Bad form (or form details), no form supplied...
		# Render the form with the error messages (if any).
	return render(request, 'rango/add_category.html', {'form': form})		
			
def add_page(request):
	try:
		cat = Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
				cat = None

	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			if cat:
				page = form.save(commit=False)
				page.category = cat 
				page.views = 0
				page.save()
				# probably better to use a redirect here.
				return category(request, category_name_slug)
		else: 
			print form.errors
	else:
		form = PageForm()

	context_dict = {'form' : form, 'category':cat}

	return render(request, 'rango/add_page.html', context_dict)								

def register(request):

	# A boolean value for telling the template whether the registration was successful.
	# Set tp false initially. Code changes value tp True when the registration succeeds.
	registered = False

	# If its a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt tp grab the information from the raw form information.
		# Note that we make use of both the UserForm and the UserProfileForm.
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		# if the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
			# save the users form data to the database
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user

			# Now deal with the profile picture
			# Did the user provide a profile picture??
			# If so we need to GET it from the input form and put it in the userProfile model.
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			# Now we save the UserProfile model instance.
			profile.save()

			# update our variable to tell the template registration was successful.
			registered = True

		# invalid form or forms - mistakes or something else?
		# print problems to the terminal.
		# Theyll also be shown to the user.
		else: 
			print user_form.errors, profile_form.errors

	# Not a HTTP POST, so we render our form using two ModelForm instances,
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	# Render the template depending on the context.
	return render(request, 
			'rango/register.html', 
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )	


def user_login(request):
	# if the request is a HTTP POST, try to pull out the relevant info.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = request.POST['username']
		password = request.POST['password']

		# Use Django's machinery to attempt to see if the username/password
		# combo is valid - a User object is returned if it is.

		user = authenticate(username=username, password=password)

		# if we have a User object, the details are correct,
		# if none then no user with matching credentials 
		if user:
			# is the account active? It could have been disabled 
			if user.is_active:
				# if the account is active and valid then the user can 
				# be logged in. We'll send the user back to the home page
				login(request, user)
				return HttpResponseRedirect('/rango/')

			else:
				# A inactive account was used => no login
				return HttpResponse("Your Rango account is disabled.")

		else:
			# Bad login details were provided => no login
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")

	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be an HTTP GET.
	else:
		# No context variable to pass to the template system, hence the 
		# blank dictionary object...
		return render(request, 'rango/login.html', {})		

@login_required
def restricted(request):
	return HttpResponse("Since you're logged in, you can see this text!")	

@login_required
def user_logout(request):
	# Since we know that the user is logged in we can just log them out
	logout(request)

	# Take the user back to the homepage
	return HttpResponseRedirect('/rango/')










