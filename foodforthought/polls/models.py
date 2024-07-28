from django.db import models

# Create your models here.
class Recipe(models.Model):
    """This class represents a recipe in our poll app.

    Attributes:
    - :param recipe_text: The main question for the poll.
    - :type: Character text field max length of 200.
    - :param pub_date: The timestamp when the recipe question was created.
    - :type: Datetime
    """
    recipe_text = models.CharField('recipe', max_length=200)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        """Constructor method for string of text for recipe.

            :return: recipe_text.
            :rtype: str.
        """
        return self.recipe_text


class Choice(models.Model):
    """Class for Choice in the poll, with foreign key linking to a recipe.
        
        Attributes:
        - :param recipe: Links to the :class: Recipe.
        - :type: Character text field max length of 200.
        - :param choice_text: Text of the choice available to choose from in the poll.
        - :type: Character text field max length of 200.
        - :param votes: Number of votes for the specific choice in that poll question.
        - :type: int.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    choice_text = models.CharField('choice', max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        """Constructor method for string of text for choice.

            :return: choice_text.
            :rtype: str.
        """
        return self.choice_text