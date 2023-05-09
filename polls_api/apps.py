from django.apps import AppConfig

class PollApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls_api'

    def ready(self):
        import polls_api.signals
