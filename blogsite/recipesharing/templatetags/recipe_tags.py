import markdown
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
# from recipeimages.models import RecipeImage
# from taggit.managers import TaggableManager

from ..models import Recipe

register = template.Library()


@register.simple_tag
def total_recipes():
    return Recipe.published.count()


@register.inclusion_tag('recipesharing/recipe/latest_recipes.html')
def show_latest_recipes(count=5):
    latest_recipes = Recipe.published.order_by('-publish')[:count]
    return {'latest_recipes': latest_recipes}


@register.simple_tag
def get_most_commented_recipes(count=5):
    return Recipe.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

# @register.inclusion_tag('recipeimages/recipeimage/list_recipeimages.html')
# def similar_images(count=5):
#     # similar_images = RecipeImage.objects.filter(tags__in=recipeimage.tags.all())
#     # return {'recipeimages:list'}
#     recipeimage_tags = set(recipeimage.tags.all())
#     similar_images = []

#     for other_recipeimage in RecipeImage.objects.all():
#         other_tags = set(other_recipeimage.tags.all())
#         similarity = len(recipeimage_tags & other_tags) / len(recipeimage_tags | other_tags)

#         if similarity > 0:
#             similar_images.append((other_recipeimage, similarity))

#     similar_images.sort(key=lambda x: x[1], reverse=True)
#     return similar_images
