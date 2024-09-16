from django.shortcuts import get_object_or_404, render
from .models import Recipe, Review
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .forms import CommentForm, EmailRecipeForm, SearchForm, ReviewForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity

# Create your views here.
def recipe_list(request, tag_slug=None):
    recipe_list = Recipe.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        recipe_list = recipe_list.filter(tags__in=[tag])
    # Pagination with 3 posts per page
    paginator = Paginator(recipe_list, 3)
    page_number = request.GET.get('page')
    try:
        recipes = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer get the first page
        recipes = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range get last page of results
        recipes = paginator.page(paginator.num_pages)
    return render(
        request,
        'recipesharing/recipe/list.html',
        {
            'recipes': recipes,
            'tag': tag
        }
    )


def recipe_detail(request, year, month, day, recipe):
    recipe = get_object_or_404(
        Recipe,
        status=Recipe.Status.PUBLISHED,
        slug=recipe,
        publish__year=year,
        publish__month=month,
        publish__day=day)
    # List of active comments for this post
    comments = recipe.comments.filter(active=True)
    # Form for users to comment
    form = CommentForm()
    # List of active ratings
    reviews = recipe.reviews.filter(active=True)
    # Form for ratings
    form = ReviewForm()
    # List of similar posts
    recipe_tags_ids = recipe.tags.values_list('id', flat=True)
    similar_recipes = Recipe.published.filter(tags__in=recipe_tags_ids).exclude(id=recipe.id)
    similar_recipes = similar_recipes.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(
        request,
        'recipesharing/recipe/detail.html',
        {
            'recipe': recipe,
            'comments': comments,
            'form': form,
            'similar_recipes': similar_recipes,
            'reviews': reviews
        }
    )

class RecipeListView(ListView):
    """
    Alternative post list view
    """
    queryset = Recipe.published.all()
    context_object_name = 'recipes'
    paginate_by = 3
    template_name = 'recipesharing/recipe/list.html'

def recipe_share(request, recipe_id):
    # Retrieve post by id
    recipe = get_object_or_404(
        Recipe,
        id=recipe_id,
        status=Recipe.Status.PUBLISHED
    )
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailRecipeForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            recipe_url = request.build_absolute_uri(
                recipe.get_absolute_url()
            )
            subject = (
                f"{cd['name']} ({cd['email']}) "
                f"recommends you read {recipe.title}"
            )
            message = (
                f"Read {recipe.title} at {recipe_url}\n\n"
                f"{cd['name']}\'s comments: {cd['comments']}"
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd['to']]
            )
            sent = True
    else:
        form = EmailRecipeForm()
    return render(
        request,
        'recipesharing/recipe/share.html',
        {
            'recipe': recipe,
            'form': form,
            'sent': sent
        }
    )

@require_POST
def recipe_comment(request, recipe_id):
    recipe = get_object_or_404(
        Recipe,
        id=recipe_id,
        status=Recipe.Status.PUBLISHED
    )
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a Comment object without saving it to the database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.recipe = recipe
        # Save the comment to the database
        comment.save()
    return render(
        request,
        'recipesharing/recipe/comment.html',
        {
            'recipe': recipe,
            'form': form,
            'comment': comment
        }
    )

def recipe_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = (
                Recipe.published.annotate(
                    similarity=TrigramSimilarity('title', query),
                )
                .filter(similarity__gt=0.1)
                .order_by('-similarity')
            )
    return render(
        request,
        'recipesharing/recipe/search.html',
        {
            'form': form,
            'query': query,
            'results': results
        }
    )

@require_POST
def recipe_review(request, recipe_id):
    recipe = get_object_or_404(
        Recipe,
        id=recipe_id,
        status=Recipe.Status.PUBLISHED
    )
    review = None
    # A rating was posted
    form = ReviewForm(data=request.POST)
    if form.is_valid():
        # Create a Comment object without saving it to the database
        review = form.save(commit=False)
        # Assign the post to the comment
        review.recipe = recipe
        # Save the comment to the database
        review.save()
    return render(
        request,
        'recipesharing/recipe/review.html',
        {
            'recipe': recipe,
            'form': form,
            'review': review
        }
    )