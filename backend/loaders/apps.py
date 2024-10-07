from django.apps import AppConfig


class LoadersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loaders'

    def ready(self):
        import loaders.signals
