from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['nomi', 'tavsifi', 'tayyorlash_vaqti', 'muallif']
