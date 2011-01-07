from django.conf.urls.defaults import *

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from core.api.handlers import ContactHandler
from core.api.handlers import GroupHandler
from core.api.handlers import JotDailyHandler, JotContactHandler, JotGroupHandler
from core.api.handlers import UserHandler


#auth = HttpBasicAuthentication(realm='JohnJot')
#ad = { 'authentication': auth }
ad = {}
# Link each handler with the authentication protocol as a Resource
contact_handler = Resource(handler=ContactHandler, **ad)
group_handler = Resource(handler=GroupHandler, **ad)
user_handler = Resource(handler=UserHandler, **ad)
jot_daily_handler = Resource(handler=JotDailyHandler, **ad)
jot_contact_handler = Resource(handler=JotContactHandler, **ad)
jot_group_handler = Resource(handler=JotGroupHandler, **ad)

urlpatterns = patterns('',
    # create, fetch, modify, delete, user account.
    url(r'users/(?P<username>[^/]+)', user_handler, {'emitter_format': 'json'}),
    url(r'users/', user_handler),
    ### Might have to merge the two URI below. ###
    # fetch all contacts for a user (use GET) 
    #url(r'users/(?P<username>[^/]+/)/contacts/', contact_handler),
    # create, fetch, modify, delete, a contact.
    #url(r'users/(?P<username>[^/]+/)/contacts/(?P<contact_id>[^/]+)/',
    #    contact_handler),
    # fetch, create jot for a given contact
    #url(r'users/(?P<username>[^/]+)/contacts/(?P<contact_id>[^/]+)/jots/',
    #    jot_contact_handler),
    # create, fetch, modify, delete, a jot.
    #url(r'^jots/(?P<jot_id>[^/]+)/', jot_handler),
)

