from django.apps import AppConfig


class PollsConfig(AppConfig):
    """
    Configuration class for the 'polls' application.

    Attributes:
        default_auto_field (str): Specifies the default type of primary key field as BigAutoField.
        name (str): The full Python import path to the application ('polls').
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
