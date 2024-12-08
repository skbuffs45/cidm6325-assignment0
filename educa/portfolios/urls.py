from django.urls import path
from . import views

app_name = 'portfolios'
urlpatterns = [
    path(
        'mine/',
        views.ManagePortfolioListView.as_view(),
        name='manage_portfolio_list'
    ),
    path(
        'create/',
        views.PortfolioCreateView.as_view(),
        name='portfolio_create'
    ),
    path(
        '<pk>/edit/',
        views.PortfolioUpdateView.as_view(),
        name='portfolio_edit'
    ),
    path(
        '<pk>/delete/',
        views.PortfolioDeleteView.as_view(),
        name='portfolio_delete'
    ),
    path(
        '<pk>/portfolio/',
        views.CoursePortfolioUpdateView.as_view(),
        name='course_portfolio_update'
    ),
    path(
        'portfolio/<int:portfolio_id>/content/<model_name>/create/',
        views.PortfolioContentCreateUpdateView.as_view(),
        name='portfolio_content_create'
    ),
    path(
        'portfolio/<int:portfolio_id>/content/<model_name>/<id>/',
        views.PortfolioContentCreateUpdateView.as_view(),
        name='portfolio_content_update'
    ),
    path(
        'content/<int:id>/delete/',
        views.PortfolioContentDeleteView.as_view(),
        name='portfolio_content_delete'
    ),
    path(
        'portfolio/<int:portfolio_id>/',
        views.PortfolioContentListView.as_view(),
        name='portfolio_content_list'
    ),
    path(
        'portfolio/<int:pk>/detail/',
        views.PortfolioDetailView.as_view(),
        name='portfolio_detail'
    ),
    # path(
    #     'portfolio/<slug:portfolio>/',
    #     views.PortfolioListView.as_view(),
    #     name='course_list_portfolio'
    # ),
    # path(
    #     '<slug:slug>/',
    #     views.PortfolioDetailView.as_view(),
    #     name='portfolio_detail'
    # ),
]