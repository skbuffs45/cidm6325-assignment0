from django import forms
from .models import RecipeImage
import requests
from django.core.files.base import ContentFile
from django.utils.text import slugify

class RecipeImageCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError(
                'The given URL does not match valid image extensions.'
            )
        return url
    def save(self, force_insert=False, force_update=False, commit=True):
        recipeimage = super().save(commit=False)
        recipeimage_url = self.cleaned_data['url']
        name = slugify(recipeimage.title)
        extension = recipeimage_url.rsplit('.', 1)[1].lower()
        recipeimage_name = f'{name}.{extension}'
        # download image from the given URL
        response = requests.get(recipeimage_url)
        recipeimage.recipeimage.save(
            recipeimage_name,
            ContentFile(response.content),
            save=False
        )
        if commit:
            recipeimage.save()
        return recipeimage