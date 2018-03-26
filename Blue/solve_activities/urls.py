from django.urls import path, include
from Blue import views as blue_views
from .import views

app_name = 'solve_activities'

urlpatterns = [
    path('', blue_views.HomePage.as_view(), name='home'),
]
