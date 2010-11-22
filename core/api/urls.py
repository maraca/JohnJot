from django.conf.urls.defaults import *

from piston.resource import Resource
from piston.authentication import OAuthAuthentication
from core.api.handlers import ContactHandler


auth = OAuthAuthentication(realm='JohnJot')
ad = { 'authentication': auth }


contact_handler = Resource(handler=ContactHandler, **ad)

urlpatterns = patterns('',
    url(r'^contact/(?P<contact_id>[^/]+)/', contact_handler),
    url(r'^contacts/', contact_handler),
)

# OAuth
urlpatterns += patterns('piston.authentication',
    url(r'^oauth/request_token/$', 'oauth_request_token', name='oauth_request_token'),
    url(r'^oauth/authenticate/$', 'oauth_user_auth', name='oauth_user_auth'),
    url(r'^oauth/access_token/$', 'oauth_access_token', name='oauth_access_token'),
)