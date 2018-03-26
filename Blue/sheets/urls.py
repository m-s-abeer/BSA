from django.urls import include, path
from . import views

app_name = 'sheets'
urlpatterns = [
    path('', views.ListSheets.as_view(), name='home'),
    path('<slug:slug>/', views.SheetView.as_view(), name='main_sheet'),
    path('<slug:slug>/join', views.JoinSheetView.as_view(), name='join_sheet'),
]
