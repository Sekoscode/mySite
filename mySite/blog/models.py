from django.db import models

# Model creation
class Post(models.Model):
    """
    Represents a blog post in the application.

    Fields:
        id (AutoField): Primary key for the post.
        title (CharField): The title of the blog post (max length 140).
        body (TextField): The main content of the blog post.
        signature (CharField): A default closing or signature message.
        date (DateTimeField): The date and time the post was created or published.
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="You can always change your mind!")
    date = models.DateTimeField()

    def __str__(self):
        """
        Returns a human-readable representation of the Post instance,
        which is the post's title.
        """
        return self.title
