from django.forms.models import inlineformset_factory
from .models import Portfolio
from courses.models import Course

PortfolioFormSet = inlineformset_factory(
    Course,
    Portfolio,
    fields=['title', 'overview'],
    extra=2,
    can_delete=True
)