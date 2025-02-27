from django.urls import path
from .views import index, RecipeListView, RecipeDetailView

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    #path('recipe/<int:pk>', recipe_2, name='recipe-detail'),
]

app_name = "ledger"