from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(), name='student_registration'),
    path('enroll-course/', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/', views.StudentCourseListView.as_view(), name='student_course_list'),
    path('course/<pk>/', cache_page(60 * 15)(views.StudentCourseDetailView.as_view()), name='student_course_detail'),
    path('course/<pk>/<module_id>/', cache_page(60 * 15)(views.StudentCourseDetailView.as_view()), name='student_course_detail_module'),
    # path('course/<pk>/<portfolio_id>/', views.StudentCourseDetailView.as_view(), name='student_course_detail_portfolio'),
    # path('portfoliomine/', views.ManagePortfolioListView.as_view(), name='manage_portfolio_list'),
    # path('portfoliocreate/', views.PortfolioCreateView.as_view(), name='portfolio_create'),
    # path('<pk>/portfolioedit/', views.PortfolioUpdateView.as_view(), name='portfolio_edit'),
    # path('<pk>/portfoliodelete/', views.PortfolioDeleteView.as_view(), name='portfolio_delete'),
    # path('course/<pk>/portfoliomine/', views.CoursePortfolioUpdateView.as_view(), name='course_portfolio_update'),
#     path('portfolio/<int:portfolio_id>/content/<model_name>/create/', views.PortfolioContentCreateUpdateView.as_view(), name='portfolio_content_create'),
#     path('portfolio/<int:portfolio_id>/content/<model_name>/<id>/', views.PortfolioContentCreateUpdateView.as_view(),name='portfolio_content_update'),
]



