from django.urls import path

from .views import index

urlpatterns = [
    #the url, function name, name for a specific url
    path('', index, name='index'),
    #path('list', recipe_list, name='list') 
]

app_name = "ledger"