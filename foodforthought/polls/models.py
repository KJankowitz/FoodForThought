from django.db import models

# Create your models here.
class Recipe(models.Model):
    '''Class for recipe, with fields recipe_text and pub_date. '''
    recipe_text = models.CharField('recipe', max_length=200)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        '''Returns recipe text.'''
        return self.recipe_text


class Choice(models.Model):
    '''Class for Choice, with foreign key linking to a recipe.'''
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    choice_text = models.CharField('choice', max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        '''Returns the choice_text of choice model.'''
        return self.choice_text