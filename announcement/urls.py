from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views

app_name = 'announcement'
urlpatterns = [
    path('add/', login_required(views.AddAnnouncement.as_view(template_name="announcement/add.html")),name='add_announcement'),
    path('all/', views.AnnouncementList.as_view(), name='all_announcement')

]
