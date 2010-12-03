import os
import sys

# Redirects the output to the Apache errors log
sys.stdout = sys.stderr

# Adds the current path to the PYTHON PATH
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
