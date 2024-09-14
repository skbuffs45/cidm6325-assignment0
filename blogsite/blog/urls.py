from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    # post views
    # https://myblog.com/blog/
    path('', views.post_list, name='post_list'),
    # https://myblog.com/blog/5/
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]
