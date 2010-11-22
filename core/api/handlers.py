from piston.handler import BaseHandler, AnonymousBaseHandler
from core.models import Contact

class ContactHandler(BaseHandler):
    allowed_methods = ('GET',)
    exclude = ('owner', 'date_created', 'last_edit')
    model = Contact   

    def read(self, request, contact_id=None):
        """
        Returns a single post if `contact_id` is given,
        otherwise a subset.
        """
        base = Contact.objects
        
        if contact_id:
            return base.get(pk=contact_id)
        else:
            return base.all() # Or base.filter(...)
        
# http://domain/api/1.0
class RootHandlerAnonymous(AnonymousBaseHandler):
    allowed_methods = ('GET',)

    def read(self, request):
        kwargs = {'username': request.user.username}
        root = {'api-version': '1.0'}
        return root

# http://domain/api/1.0
class RootHandler(BaseHandler):
    allowed_methods = ('GET',)
    anonymous = RootHandlerAnonymous

    def read(self, request):
        kwargs = {'username': request.user.username}
        root = {'api-version': '1.0'}
        return root
