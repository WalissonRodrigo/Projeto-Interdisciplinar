<<<<<<< HEAD
from django.conf.urls import url
from simplemooc.core.views import *
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contato/$', contact, name='contact'),
]
=======
from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
)
>>>>>>> f2e683044aaafdb905a72a34bad0582a9ae5a7ed
