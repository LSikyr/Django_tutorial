from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Init Users app
    """
    name = 'users'

    def ready(self):
        import users.signals # pylint: disable=W0611
