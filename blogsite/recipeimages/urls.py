from django.urls import path
from . import views

app_name = 'recipeimages'
urlpatterns = [
    path('create/', views.recipeimage_create, name='create'),
    path('detail/<int:id>/<slug:slug>/', views.recipeimage_detail, name='detail'),
]