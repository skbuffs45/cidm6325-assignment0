from django import forms
from django.forms.models import inlineformset_factory
from courses.models import Course, Module

class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.none(),
        widget=forms.HiddenInput
    )
    #def __init__(self, form)
    def __init__ (self, *args, **kwargs):
        super(CourseEnrollForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()

# PortfolioFormSet = inlineformset_factory(
#     Course,
#     Portfolio,
#     fields=['title', 'date', 'overview'],
#     extra=2,
#     can_delete=True
# )