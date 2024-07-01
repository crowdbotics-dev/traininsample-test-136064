"""
WSGI config for tstprdstageapp1_de_136064 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "tstprdstageapp1_de_136064.settings"
)

application = get_wsgi_application()
