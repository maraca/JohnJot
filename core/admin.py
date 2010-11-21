from django.contrib import admin

from core.models import Group
from core.models import Contact
from core.models import JotDaily
from core.models import JotGroup
from core.models import JotContact


admin.site.register(Group)
admin.site.register(Contact)
admin.site.register(JotDaily)
admin.site.register(JotGroup)
admin.site.register(JotContact)
