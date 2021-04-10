from django.apps import AppConfig


class ContactappConfig(AppConfig):
    name = 'contactapp'

    def ready(self):
        import contactapp.signals
