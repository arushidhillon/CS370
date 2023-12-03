from django.apps import AppConfig

# This function connects the user's profile model to the user model automatically by calling signals.py file
class ProfilepageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profilepage"
    def ready(self):
        import profilepage.signals