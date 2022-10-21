from django.shortcuts import render, redirect

from recipes_exam_november_2020.recipes.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from recipes_exam_november_2020.recipes.models import Recipe


def index(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'base/index.html', context)


def create_recipe(request):
    if request.method == 'GET':
        form = CreateRecipeForm()
    else:
        form = CreateRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'recipes/create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = EditRecipeForm(instance=recipe)
    else:
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'recipes/edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':

        context = {
            'recipe': recipe,
            'form': DeleteRecipeForm(instance=recipe),
        }

        return render(request, 'recipes/delete.html', context)
    else:
        recipe.delete()
        return redirect('index')


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = [ingredient for ingredient in recipe.ingredients.split(',')]

    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }

    return render(request, 'recipes/details.html', context)
