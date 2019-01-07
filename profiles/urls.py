from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views
from . import forms

app_name = 'profiles'
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
