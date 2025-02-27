from django.urls import path
from .views import index, recipe_list, recipe_1, recipe_2, RecipeListView

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', recipe_1, name='recipe-detail'),
    #path('recipe/<int:pk>', recipe_2, name='recipe-detail'),
]

app_name = "ledger"