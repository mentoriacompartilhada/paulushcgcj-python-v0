"""Basic web app project"""
from django.apps import AppConfig

class HelloConfig(AppConfig):
    """Main class of the project"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hello'
