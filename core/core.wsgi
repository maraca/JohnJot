import os
import sys

# Redirects the output to the Apache errors log
sys.stdout = sys.stderr

# Adds the current path to the PYTHON PATH
core_dir = os.path.dirname(os.path.abspath(__file__))
if core_dir in sys.path:
    sys.path.append(core_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
