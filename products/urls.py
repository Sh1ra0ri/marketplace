from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list),
    path('product/', views.product_create),
    path('product/<int:pk>/', views.product_change),
    path('<int:pk>/', views.product_detail),
]
