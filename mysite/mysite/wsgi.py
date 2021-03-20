"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
sys.path.append(BASE_DIR)

application = get_wsgi_application()
