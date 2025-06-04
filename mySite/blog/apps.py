from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration class for the 'blog' application.

    Attributes:
        default_auto_field (str): Specifies the type of auto-generated primary key field to use by default.
        name (str): The full Python path to the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
