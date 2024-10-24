from django.urls import path
from . import views

app_name = 'recipeimages'
urlpatterns = [
    path('create/', views.recipeimage_create, name='create'),
    path('detail/<int:id>/<slug:slug>/', views.recipeimage_detail, name='detail'),
    path('', views.recipeimage_list, name='list'),
    path('like/', views.recipeimage_like, name='like'),
    path('tag/<slug:tag_slug>/', views.recipeimage_list, name='recipeimage_list_by_tag'),
]