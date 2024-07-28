from django.db import models

# Create your models here.

class Post(models.Model):
    """This class represents a recipe in our blog app.

    Attributes:
    - :param title: The main title for the recipe.
    - :type: Character text field max length of 140.
    - :param body: The body text of the recipe.
    - :type: Character text field.
    - :param signature: Signature added to the end of every recipe blog entry.
    - :type: Character text field max length of 140.
    - :param date: Date the blog recipe entry was captured.
    - :type: Datetime.
    """
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Bon appetit - Kardo")
    date = models.DateTimeField()


    def __str__(self):
        """Constructor method for string of text for blog title.

            :return: title.
            :rtype: str.
        """
        return self.title