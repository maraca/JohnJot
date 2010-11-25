from piston.handler import BaseHandler
from core.models import Contact

class ContactHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('owner', 'date_created', 'last_edit')
    model = Contact   

    def read(self, request, contact_id=None):
        queryset = Contact.objects.filter(owner=request.user)
                
        if contact_id:
            return queryset.filter(pk=contact_id)
        return queryset
