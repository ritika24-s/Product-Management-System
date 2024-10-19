from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # from .management.commands import create_groups
        # create_groups.Command()
        import users.signals
