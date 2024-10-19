from django.contrib import admin
from .models import RecipeImage

@admin.register(RecipeImage)
class RecipeImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'recipeimage', 'created']
    list_filter = ['created']