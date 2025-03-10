from django.db import models
from django.urls import reverse 


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk]) 


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(default='Unknown', max_length=50, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk]) 
    

class RecipeIngredient(models.Model):
    quantity = models.IntegerField(null=True)
    ingredient = models.ForeignKey(Ingredient, 
                                   on_delete=models.SET_NULL, 
                                   null=True, 
                                   related_name = 'recipe')
    recipe = models.ForeignKey(Recipe, 
                               on_delete=models.SET_NULL, 
                               null=True, 
                               related_name='ingredients')
    
    @property
    def get_quantity(self):
        return self.quantity