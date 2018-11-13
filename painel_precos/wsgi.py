"""
WSGI config for painel_precos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import platform
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if platform.system() == 'Windows':
    import sys

    activate_this = os.path.join(BASE_DIR, 'venv', 'Scripts', 'activate_this.py')
    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))

    sys.path.append(os.path.dirname(__file__))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'painel_precos.settings')

application = get_wsgi_application()
