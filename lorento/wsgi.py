"""
WSGI config for lorento project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lorento.settings')


class HealthCheckMiddleware:
    """WSGI middleware to handle /healthz before Django for Render."""
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if environ.get("PATH_INFO") == "/healthz":
            start_response("200 OK", [("Content-Type", "text/plain")])
            return [b"OK"]
        return self.app(environ, start_response)


application = get_wsgi_application()
application = HealthCheckMiddleware(application)
