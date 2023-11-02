from django.apps import AppConfig


class ProfilepageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profilepage"

class UsersConfig(AppConfig):
    name = 'users'

#imports signals.py
    def ready(self):
        import users.signals