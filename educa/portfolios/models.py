from django.contrib.auth.models import User
from django.db import models
from courses.models import Subject, Course, Module
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .fields import OrderField

# Create your models here.
class Portfolio(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='portfolios_created',
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course, related_name='portfolios', on_delete=models.CASCADE
    )
    instructors = models.ManyToManyField(
        User,
        related_name='course_portfolios',
        blank=True
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    order = OrderField(blank=True, for_fields=['course'])
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return f'{self.order}. {self.title}'

class PortfolioContent(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        related_name='portfoliocontents',
        on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            'model__in':('portfoliotext', 'portfoliovideo', 'portfolioimage', 'portfoliofile')
        }
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['portfolio'])
    class Meta:
            ordering = ['order']

class PortfolioItemBase(models.Model):
    owner = models.ForeignKey(User,
        related_name='%(class)s_related',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
    def __str__(self):
        return self.title
class PortfolioText(PortfolioItemBase):
    content = models.TextField()
class PortfolioFile(PortfolioItemBase):
    file = models.FileField(upload_to='files')
class PortfolioImage(PortfolioItemBase):
    file = models.FileField(upload_to='images')
class PortfolioVideo(PortfolioItemBase):
    url = models.URLField()
