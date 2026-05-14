from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('me/', views.me),
]
