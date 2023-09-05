import os
from django.core.wsgi import get_wsgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable to your project's settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')

# Create a WSGI application instance
application = get_wsgi_application()
