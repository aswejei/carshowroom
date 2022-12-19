from django.apps import AppConfig


class CarshowroomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carshowroom'

    def ready(self):
        try:
            from . import signals
        except ImportError:
            pass
