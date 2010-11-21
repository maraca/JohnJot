import os
import sys

# Redirects errors to output
sys.stdout = sys.stderr

# Adds the current path to the PYTHON PATH
path = os.path.dirname(os.path.dirname(__file__))
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


