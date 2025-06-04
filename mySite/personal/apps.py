from django.apps import AppConfig


class PersonalConfig(AppConfig):
    """
    Configuration class for the 'personal' application.

    Attributes:
        default_auto_field (str): Specifies the default type for auto-created primary key fields.
        name (str): The full Python path to the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personal'
