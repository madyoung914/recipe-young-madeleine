from django.urls import path
from .views import RecipeListView, RecipeCreateView, RecipeUpdateView
from .views import RecipeImageCreateView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeUpdateView.as_view(), name='recipe-detail'),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/add_image', RecipeImageCreateView.as_view(),
         name='recipe-image-create'),
]

app_name = "ledger"
