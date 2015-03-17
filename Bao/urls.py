from django.conf.urls import patterns, url
from Bao import views

urlpatterns = patterns('',

	url(r'^$', views.index, name = 'index_Bao'),

	url(r'^bao_rules/$', views.bao_rules, name = 'bao_rules'),

	url(r'^about_us/$', views.about_us, name = 'about_us'),

	# will be the same tutorial for everyone => only one url
	url(r'^tutorial/$', views.tutorial, name='tutorial'),

	url(r'^new_game/$', views.new_game, name='new_game'),

	url(r'^register/$', views.register, name='register_Bao'),

	#url(r'^login/$', views.user_login, name='login_Bao'),

	#url(r'^logout/$', views.user_logout, name='logout_Bao'),

	#url(r'^/(?P<register_username_slug>)$', views.index, name = 'index'),
	
	url(r'^my_profile/$', views.my_profile, name='my_profile'),

	url(r'^like_tutorial/$', views.like_tutorial, name="like_tutorial"),
)

#(?P<new_game_slug>\^[a-zA-Z]+)$'