from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from djangostore.constants import LOGIN_TEMPLATE


urlpatterns = [
    path('register/', views.register_account_view, name='register'),
    path('login/', LoginView.as_view(template_name=LOGIN_TEMPLATE), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
