from django.urls import include, path
from . import views

app_name = 'sheets'
urlpatterns = [
    path('', views.ListSheets.as_view(), name='home'),
    path('<slug:slug>/', views.SheetView.as_view(), name='single'),
]
