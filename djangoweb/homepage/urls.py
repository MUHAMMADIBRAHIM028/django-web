from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/", views.user_info_view, name="user_info"),
    path("success/", views.success_view, name="success"),
    path("index/", views.index, name="index"),
]
