from django.apps import AppConfig
from django.db.models.signals import post_migrate

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from . import signals
        post_migrate.connect(signals.create_token_usuarios,sender=self)