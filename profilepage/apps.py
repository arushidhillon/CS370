from django.apps import AppConfig

#This allows newly registered user to create profiles by calling the signals.py functions
class ProfilepageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profilepage"
    def ready(self):
        import profilepage.signals