#projects url
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/Bao/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # this new tuple will look for url string patterns that match 
    # the patterns ^rango/. Once a match is made the rest of the 
    # ur; string is dealt with in the rango.urls file.
    # To do this we use the include which was imported.
    url(r'^rango/', include('rango.urls')), # NEW TUPLE

    # add a URL tuple for dealing with Bao urls 
    url(r'^Bao/', include('Bao.urls')),

    url('^accounts/register/$', MyRegistrationView.as_view(), name = 'registration_register'),
    # add tuple to deal with registration package
    (r'^accounts/', include('registration.backends.simple.urls')),
)

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root' : settings.MEDIA_ROOT}), )
