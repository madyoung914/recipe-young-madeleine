from django.db import models
from django.urls import reverse 

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk]) 

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipes/list', '') 
    #idk ab this should always link to recipes/list????
    
class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    ingredients = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True, related_name = 'ingredients')
    recipes = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True, related_name='recipes')