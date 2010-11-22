from piston.handler import BaseHandler
from core.models import Contact

class ContactHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('owner', 'date_created', 'last_edit')
    model = Contact   

    def read(self, request, contact_id=None):
        base = Contact.objects
        
        if contact_id:
            return base.get(pk=contact_id)
        else:
            return base.all()
