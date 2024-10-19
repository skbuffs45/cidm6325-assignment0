from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import RecipeImageCreateForm
from django.shortcuts import get_object_or_404
from .models import RecipeImage

def recipeimage_create(request):
    if request.method == 'POST':
        # form is sent
        form = RecipeImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_recipeimage = form.save(commit=False)
            # assign current user to the item
            # new_recipeimage.user = request.user
            new_recipeimage.save()
            messages.success(request, 'Image added successfully')
            # redirect to new created item detail view
            return redirect(new_recipeimage.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = RecipeImageCreateForm(data=request.GET)
    return render(
        request,
        'recipeimages/recipeimage/create.html',
        {'section': 'recipeimages', 'form': form}
    )

def recipeimage_detail(request, slug):
    recipeimage = get_object_or_404(RecipeImage, slug=slug)
    return render(
        request,
        'recipeimages/recipeimage/detail.html',
        {'section': 'recipeimages', 'recipeimage': recipeimage}
    )