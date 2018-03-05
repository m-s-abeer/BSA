from django.urls import include, path
from . import views

app_name = 'problems'
urlpatterns = [
    path('', views.ProblemList.as_view(), name='archive'),
    path('<slug:slug>/', views.ProblemDetail.as_view(), name='problem_detail'),
]
