from django.urls import include, path
from . import views

app_name = 'badges'
urlpatterns = [
    path('', views.BadgesList.as_view(), name='badges_list'),

]
