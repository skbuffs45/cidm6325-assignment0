from django.views.generic.list import ListView
from .models import Portfolio, PortfolioContent
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateResponseMixin, View
from .forms import PortfolioFormSet
from courses.models import Course

from django.apps import apps
from django.forms.models import modelform_factory
from django.db.models import Count
from django.views.generic.detail import DetailView

class ManagePortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolios/manage/portfolio/list.html'
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
class OwnerPortfolioMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = Portfolio
    fields = ['course', 'title', 'slug', 'overview']
    success_url = reverse_lazy('portfolios:manage_portfolio_list')
class OwnerPortfolioEditMixin(OwnerPortfolioMixin, OwnerEditMixin):
    template_name = 'portfolios/manage/portfolio/form.html'
class ManagePortfolioListView(OwnerPortfolioMixin, ListView):
    template_name = 'portfolios/manage/portfolio/list.html'
    permission_required = 'portfolios.view_portfolio'
class PortfolioCreateView(OwnerPortfolioEditMixin, CreateView):
    permission_required = 'portfolios.add_portfolio'
class PortfolioUpdateView(OwnerPortfolioEditMixin, UpdateView):
    permission_required = 'portfolios.change_portfolio'
class PortfolioDeleteView(OwnerPortfolioMixin, DeleteView):
    template_name = 'portfolios/manage/portfolio/delete.html'
    permission_required = 'portfolios.delete_portfolio'

class CoursePortfolioUpdateView(TemplateResponseMixin, View):
    template_name = 'portfolios/manage/portfolio/formset.html'
    course = None
    def get_formset(self, data=None):
        return PortfolioFormSet(instance=self.course, data=data)
    # def dispatch(self, request, pk):
    #     self.course = get_object_or_404(
    #         Course, id=pk, owner=request.user
    #     )
    #     return super().dispatch(request, pk)
    def dispatch(self, request, pk):
        self.portfolio = get_object_or_404(
            Portfolio, id=pk, owner=request.user
        )
        return super().dispatch(request, pk)
    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response(
            {'course': self.course, 'formset': formset}
        )
    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('portfolios:manage_portfolio_list')
        return self.render_to_response(
            {'course': self.course, 'formset': formset}
        # return self.render_to_response(
        #     {'portfolio': self.portfolio, 'formset': formset}
        )

class PortfolioContentCreateUpdateView(TemplateResponseMixin, View):
    portfolio = None
    model = None
    obj = None
    template_name = 'portfolios/manage/content/form.html'
    def get_model(self, model_name):
        if model_name in ['portfoliotext', 'portfoliovideo', 'portfolioimage', 'portfoliofile']:
            return apps.get_model(
                app_label='portfolios', model_name=model_name
            )
        return None
    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(
            model, exclude=['owner', 'order', 'created', 'updated']
        )
        return Form(*args, **kwargs)
    def dispatch(self, request, portfolio_id, model_name, id=None):
        self.portfolio = get_object_or_404(
            Portfolio, id=portfolio_id, owner=request.user
        )
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(
                self.model, id=id, owner=request.user
            )
        return super().dispatch(request, portfolio_id, model_name, id)
    def get(self, request, portfolio_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response(
            {'form': form, 'object': self.obj}
        )
    def post(self, request, portfolio_id, model_name, id=None):
        form = self.get_form(
            self.model,
            instance=self.obj,
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            if not id:
                # new content
                PortfolioContent.objects.create(portfolio=self.portfolio, item=obj)
            return redirect('portfolios:portfolio_content_list', self.portfolio.id)
        return self.render_to_response(
            {'form': form, 'object': self.obj}
        )

class PortfolioContentDeleteView(View):
    def post(self, request, id):
        content = get_object_or_404(
            PortfolioContent, id=id, owner=request.user,
        )
        portfolio = content.portfolio
        content.item.delete()
        content.delete()
        return redirect('portfolios:portfolio_content_list', portfolio.id)

class PortfolioContentListView(TemplateResponseMixin, View):
    template_name = 'portfolios/manage/portfolio/content_list.html'
    def get(self, request, portfolio_id):
        portfolio = get_object_or_404(
            Portfolio, id=portfolio_id, owner=request.user
        )

        portfolio_contents = PortfolioContent.objects.filter(portfolio=portfolio)

        return self.render_to_response({'portfolio': portfolio, 'portfolio_contents': portfolio_contents})

class PortfolioDetailView(LoginRequiredMixin, DetailView):
    model = Portfolio
    template_name = 'portfolios/portfolio/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = self.get_object()

        if 'portfolio_id' in self.kwargs:
            context['portfolio'] = get_object_or_404(Portfolio, id=self.kwargs['portfolio_id'])
        else:
            context['portfolio'] = Portfolio.objects.first()

        return context