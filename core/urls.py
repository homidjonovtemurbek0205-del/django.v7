from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_recipe, name='create-recipe'),
    path('update/<int:id>/', views.update_recipe, name='edit-recipe'),
    path('delete/<int:id>/', views.delete_recipe, name='delete-recipe'),
]
