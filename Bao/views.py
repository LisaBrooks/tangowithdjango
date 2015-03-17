from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Bao.models import UProfile, Game
from Bao.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from Bao.models import UProfile

def index(request):
	context_dict = {'boldmessage': "Play today and find out!"}
	
	visits = request.session.get('visits')
	if not visits:
		visits = 1
	reset_last_visit_time = False
	
	last_visit = request.session.get('last_visit')
	if last_visit:
		last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")	
	
		if(datetime.now() - last_visit_time).seconds > 0:
			# incrementing the value of the cookie
			visits = visits + 1
			# update the last visit cookie
			reset_last_visit_time = True
	else:
		# cookie last_visit doesn't exit => create it!
		reset_last_visit_time = True

	if reset_last_visit_time:
		request.session['last_visit'] = str(datetime.now())
		request.session['visits'] = visits
	context_dict['visits'] = visits	

	response = render(request, 'Bao/index.html', context_dict)

	# return a rendered response to the client
	return response

def bao_rules(request):
	return render(request, 'Bao/Bao_rules.html')

def about_us(request):
	return render(request, 'Bao/about_us.html')

def tutorial(request):
#	likes = request.session.get('likes')

	return render(request, 'Bao/tutorial.html')

@login_required
def like_tutorial(request):
	# there is only one tutorial so there is no need to check the tutorial id.
	likes = likes + 1
	return HttpResponse(likes)

@login_required
def new_game(request):
	context_dict={}

	try:
		# Can we find a game_number_slug with the given number?
		# If we can't then the .get() method raises a DoesNotExist 
		# exception. So the .get() method returns one model instance 
		# or raises an exception.

		game = Game.objects.get()
		context_dict['game_number'] = game.number

		context_dict['game']=Game

	except Game.DoesNotExist:
		# We get here if we didnt find the specified game number.
		# Don't do anything, the template new_game.html will 
		# display a "no game found" message.
		pass

	# render the response to be returned to the client.	
	return render(request, 'Bao/new_game.html', context_dict)


def register(request):#, register_username_slug):
	# A boolean that tells the template whether the regustration
	# was a success or not.
	successful_registration=False

	# Need to process the form if it is a HTTP Post
	if request.method == 'POST':
		# Need get information from both the UProfile and 
		# the UserForm. 
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		print "REGISTER POST"

		# if and only if both forms are valid the information
		# can be processed.
		if user_form.is_valid() and profile_form.is_valid():
			# save the data in the database
			user = user_form.save()
			
			# set the password that the user has provided using
			# the set_password method.
			user.set_password(user.password)
			user.save()

			# user_form has now been dealt with, now deal with
			# the information obtained via the profile_form.
			profile = profile_form.save(commit=False)
			profile.user = user

			# has the user opted to include a profile picture?
			# If so we GET it from the profile_form
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.score = 0

			# save the profile_form information in the UProfile
			# model instance.
			profile.save()

			print "HELLO LISA"
			print profile

			# Now all elements of the registration have been 
			# performed and the user is now registered. Update the 
			# boolean.
			successful_registration = True
			user=authenticate(username=user.username, password=user.password)

		# however either or both of the forms - user_form, profile_form
		# have invalid data then print the errors.
		else:
			print "ERROR!!!"
			print user_form.errors, profile_form.errors
	
	# Not a HTTP POST, therefore render our form using two ModelForm
	# instances. These forms are blank and ready for user input.
	else:
		user_form=UserForm()
		profile_form=UserProfileForm()

	if successful_registration:
		return HttpResponseRedirect('/Bao/')
	else: 
		print "Error in registration"	

	# Dependant on the context render the template.
	return render(request, 'Bao/register.html',
				{'user_form':user_form, 'profile_form':profile_form,'successful_registration':successful_registration})#, context_dict )

def user_login(request):
	# if the request is a HTTP POST, try and get the relevant info.
	if request.method == 'POST':
		# get the username and password provided by the user.
		username=request.POST['username'] 
		password=request.POST['password']

		# user authenticate() to check if username/password combo
		# is valid.
		user=authenticate(username=username, password=password)

		# if we have a user object => details were valid.
		# if not => no user matched the combo.
		if user:
			# need to make sure the account is also active.
			if user.is_active:
				# if active and valid => account can be logged in.
				login(request, user)
				# redirect user back to main page. The page will 
				# now feature content which can only be seen if 
				# registered and logged in.
				return HttpResponseRedirect('/Bao/')

			else:
			# the account was inactive => login denied.
				return HttpResponse("Your Bao account is disabled")
		else:
		# Invalid login details entered.
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")

	# the request is not a HTTP POST => display blank login form.
	else:	
		return render(request, 'Bao/login.html', {}) 	

@login_required
def user_logout(request):
	# since the user is already logged we can log them out.
	logout(request)
	# send user back to homepage
	return HttpResponseRedirect('/Bao/')			

@login_required
def my_profile(request):
	user = request.user
	up = UProfile.objects.get(user=user)

	context_dict =  {'up': up}
	return render(request, 'Bao/my_profile.html',context_dict)



