from django.apps import AppConfig


class AutogenerateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autogenerate'

    def ready(self):
        import autogenerate.signals