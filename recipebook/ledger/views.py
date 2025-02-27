from django.shortcuts import render 
from django.http import HttpResponse 
from .models import Recipe, RecipeIngredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'