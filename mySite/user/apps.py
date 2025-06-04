from django.apps import AppConfig


class UserConfig(AppConfig):
    """
    Configuration class for the 'user' application.

    Attributes:
        default_auto_field (str): Specifies the default type for auto-generated primary keys.
        name (str): The full Python import path to the application ('user').
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
