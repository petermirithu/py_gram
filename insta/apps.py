from django.apps import AppConfig


class InstaConfig(AppConfig):
    name = 'insta'

# importing signals for the app to use in creating profile page automatically
    def ready(self):
        import insta.signals

