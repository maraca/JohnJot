from piston.handler import BaseHandler
from core.models import Contact
from core.models import Group
from core.models import JotDaily, JotGroup, JotContact

class ContactHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('owner', 'date_created', 'last_edit')
    model = Contact
    
    def read(self, request, contact_id=None):
        queryset = Contact.objects.filter(owner=request.user)
                
        if contact_id:
            return queryset.filter(pk=contact_id)
        return queryset

class GroupHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('owner', 'date_created', 'last_edit')
    model = Group
    
    def read(self, request, group_id=None):
        queryset = Group.objects.filter(owner=request.user)
                
        if group_id:
            return queryset.filter(pk=group_id)
        return queryset

class JotDailyHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('owner', 'date_created', 'last_edit')
    model = JotDaily

    def read(self, request, jot_id=None):
        queryset = JotDaily.objects.filter(owner=request.user)
                
        if jot_id:
            return queryset.filter(pk=jot_id)
        return queryset

class JotContactHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('date_created', 'last_edit')
    model = JotContact

    def read(self, request, jot_id=None):
        contacts = Contact.objects.filter(owner=request.user)
        queryset = JotContact.objects.filter(contact__in=contacts)
                
        if jot_id:
            return queryset.filter(pk=jot_id)
        return queryset

class JotGroupHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('date_created', 'last_edit')
    model = JotGroup

    def read(self, request, jot_id=None):
        groups = Group.objects.filter(owner=request.user)
        queryset = JotGroup.objects.filter(group__in=groups)
                
        if jot_id:
            return queryset.filter(pk=jot_id)
        return queryset
