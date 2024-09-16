from django.urls import path
from . import views
from .feeds import LatestRecipesFeed

app_name = 'recipesharing'
urlpatterns = [
    # Recipe views
    path('', views.recipe_list, name='recipe_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', views.recipe_list, name='recipe_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:recipe>/', views.recipe_detail, name='recipe_detail'),
    path('<int:recipe_id>/share/', views.recipe_share, name='recipe_share'),
    path('<int:recipe_id>/comment/', views.recipe_comment, name='recipe_comment'),
    path('feed/', LatestRecipesFeed(), name='recipe_feed'),
    path('search/', views.recipe_search, name='recipe_search'),
    path('<int:recipe_id>/review/', views.recipe_review, name='recipe_review'),
]