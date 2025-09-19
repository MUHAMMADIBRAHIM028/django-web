# homepage/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.index, name="index"),
    path("user/", views.user_info_view, name="user_info"),
    path("success/", views.success_view, name="success"),

    # --- New Product URL ---
    path("product/", views.product_view, name="product"),
    path('accounts/login/', views.login_view),
    path('manage-products/', views.manage_products, name='manage_products'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
]
