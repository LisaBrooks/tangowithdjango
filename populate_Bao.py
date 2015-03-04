import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from BAO.models import Game #, UserProfile

def populate():
	# dummy variables

	# users
	add_user(u_name="lisa_brooks", password="bao1", pic='', score=5)
	add_user(u_name="colin_kirk", password="bao2", pic='', score=4)
	add_user(u_name="craig_reilly", password="bao3", pic='', score=4)
	add_user(u_name="sara_hillberg", password="bao4", pic='', score=7)

	# games
	add_game(num=1)
	add_game(num=2)
	add_game(num=3)
	add_game(num=4)

def add_user(u_name, password, pic, score):
	u = UserProfile.objects.get_or_create(username=u_name, password=password, picture=pic, score=score)[0]
 	return u

def add_game(num):
 	g= Game.objects.get_or_create(number=num)[0]
 	return g

# start	execution here
if __name__ == '__main__':
	print "Starting BAO population script..."
	populate()	
