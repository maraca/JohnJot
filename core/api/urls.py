from django.conf.urls.defaults import *

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from core.api.handlers import ContactHandler
from core.api.handlers import GroupHandler
from core.api.handlers import JotDailyHandler, JotContactHandler, JotGroupHandler


auth = HttpBasicAuthentication(realm='JohnJot')
ad = { 'authentication': auth }

# Link each handler with the authentication protocol as a Resource
contact_handler = Resource(handler=ContactHandler, **ad)
group_handler = Resource(handler=GroupHandler, **ad)
jot_daily_handler = Resource(handler=JotDailyHandler, **ad)
jot_contact_handler = Resource(handler=JotContactHandler, **ad)
jot_group_handler = Resource(handler=JotGroupHandler, **ad)


urlpatterns = patterns('',
    url(r'^contact/(?P<contact_id>[^/]+)/', contact_handler),
    url(r'^contacts/', contact_handler),
    url(r'^group/(?P<group_id>[^/]+)/', group_handler),
    url(r'^groups/', group_handler),
    url(r'^daily_jot/(?P<jot_id>[^/]+)/', jot_daily_handler),
    url(r'^daily_jots/', jot_daily_handler),
    url(r'^contact_jot/(?P<contact_id>[^/]+)/', jot_contact_handler),
    url(r'^contact_jots/', jot_contact_handler),
    url(r'^group_jot/(?P<group_id>[^/]+)/', jot_group_handler),
    url(r'^group_jots/', jot_group_handler),
)
