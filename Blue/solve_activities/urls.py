from django.urls import path, include
from Blue import views

app_name = 'solve_activities'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]
