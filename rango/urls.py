# application url

from django.conf.urls import patterns, url
from django.conf.urls.static import static
from rango import views
 
urlpatterns = patterns('', 
	url(r'^$', views.index, name='index_rango'),

	url(r'^about/$', views.about, name ='about_rango'),

	url(r'^add_category/$', views.add_category, name='add_category'),

	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),

	url(r'^register/$', views.register, name = 'register_rango'),

	url(r'^login/$', views.user_login, name='login_rango'),

	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),

	url(r'^restricted/', views.restricted, name='restricted'),

	url(r'^logout/$', views.user_logout, name='logout_rango'),

	#url(r'^category/(?P<category_name_url>\w+)$', views.category, name='category'),
)  