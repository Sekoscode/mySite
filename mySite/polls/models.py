from django.db import models


class Question(models.Model):
    """
    Represents a poll question.

    Fields:
        question_text (CharField): The text of the question (max 200 characters).
        pub_date (DateTimeField): The date and time the question was published.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Returns a human-readable string representation of the Question,
        which is its question text.
        """
        return self.question_text


class Choice(models.Model):
    """
    Represents a choice or answer to a specific poll question.

    Fields:
        question (ForeignKey): The related Question object (many-to-one relationship).
        choice_text (CharField): The text of the choice (max 200 characters).
        votes (IntegerField): Number of votes this choice has received (default is 0).
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns a human-readable string representation of the Choice,
        which is its choice text.
        """
        return self.choice_text
