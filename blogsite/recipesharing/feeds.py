import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Recipe

class LatestRecipesFeed(Feed):
    title = 'My Recipes'
    link = reverse_lazy('recipesharing:recipe_list')
    description = 'Newest recipes I have posted.'
    def items(self):
        return Recipe.published.all()[:5]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)
    def item_pubdate(self, item):
        return item.publish