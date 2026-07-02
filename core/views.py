from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm

def home(request):
    query = request.GET.get('q', '')
    if query:
        recipes = Recipe.objects.filter(nomi__icontains=query)
    else:
        recipes = Recipe.objects.all()
        
    total_recipes = recipes.count()
    
    context = {
        'recipes': recipes,
        'total_recipes': total_recipes,
        'query': query
    }
    return render(request, 'index.html', context)

def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RecipeForm()
    return render(request, "create-receipt.html", {'form': form})

def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "create-receipt.html", {'form': form, 'recipe': recipe})

def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        recipe.delete()
        return redirect("home")
    return render(request, "delete-confirm.html", {'recipe': recipe})
