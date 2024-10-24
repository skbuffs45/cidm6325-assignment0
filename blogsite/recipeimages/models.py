from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from taggit.managers import TaggableManager

class Tag(models.Model):
    name = models.CharField(max_length=50)

class RecipeImage(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='recipeimages_created',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000)
    recipeimage = models.ImageField(upload_to='recipeimages/%Y/%m/%d/')
    description = models.TextField(blank=True)
    # tag = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    # users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='recipeimages_liked', blank=True)
    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('recipeimages:detail', args=[self.id, self.slug])
