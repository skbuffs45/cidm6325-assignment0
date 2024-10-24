from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import RecipeImageCreateForm
from django.shortcuts import get_object_or_404
from .models import RecipeImage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from taggit.models import Tag

@login_required
def recipeimage_create(request):
    if request.method == 'POST':
        # form is sent
        form = RecipeImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_recipeimage = form.save(commit=False)
            # assign current user to the item
            new_recipeimage.user = request.user
            new_recipeimage.save()
            #save tags
            tags = form.cleaned_data['tags']
            new_recipeimage.tags.set(tags)
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

def recipeimage_detail(request, id, slug):
    recipeimage = get_object_or_404(RecipeImage, id=id, slug=slug)
    return render(
        request,
        'recipeimages/recipeimage/detail.html',
        {'section': 'recipeimages', 'recipeimage': recipeimage}
    )

@login_required
def recipeimage_list(request, tag_slug=None):
    recipeimages = RecipeImage.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        recipeimages = recipeimages.filter(tags__in=[tag])
    paginator = Paginator(recipeimages, 8)
    page = request.GET.get('page')
    recipeimages_only = request.GET.get('recipeimages_only')
    try:
        recipeimages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        recipeimages = paginator.page(1)
    except EmptyPage:
        if recipeimages_only:
            # If AJAX request and page out of range
            # return an empty page
            return HttpResponse('')
        # If page out of range return last page of results
        recipeimages = paginator.page(paginator.num_pages)
    if recipeimages_only:
        return render(
            request,
            'recipeimages/recipeimage/list_recipeimages.html',
            {'section': 'recipeimages', 'recipeimages': recipeimages}
        )
    return render(
            request,
            'recipeimages/recipeimage/list.html',
            {'section': 'recipeimages', 'recipeimages': recipeimages, 'tag': tag}
    )

@login_required
@require_POST
def recipeimage_like(request):
    recipeimage_id = request.POST.get('id')
    action = request.POST.get('action')
    if recipeimage_id and action:
        try:
            recipeimage = RecipeImage.objects.get(id=recipeimage_id)
            if action == 'like':
                recipeimage.users_like.add(request.user)
            else:
                recipeimage.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except RecipeImage.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})