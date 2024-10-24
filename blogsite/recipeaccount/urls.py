from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    # path('recipelogin/', views.user_recipelogin, name='recipelogin'),
    path('recipelogin/', auth_views.LoginView.as_view(), name='recipelogin'),
    path('recipelogout/', auth_views.LogoutView.as_view(), name='recipelogout'),
    path('', views.recipedashboard, name='recipedashboard'),
]