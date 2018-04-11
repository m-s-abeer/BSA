from django.urls import include, path
from . import views
from solve_activities import views as solve_views

app_name = 'problems'
urlpatterns = [
    path('', views.ProblemList.as_view(), name='archive'),
    path('<slug:slug>/', views.ProblemDetail.as_view(), name='problem_detail'),
    path('<slug:slug>/solve/', solve_views.SolveConfirmation.as_view(), name='problem_solved'),
    path('<slug:slug>/confirmed', solve_views.ProblemSolvedXHR, name='join_sheet_xhr'),
]
