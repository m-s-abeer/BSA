from django.shortcuts import render
from django.views import generic
from .models import Badge
# Create your views here.



class BadgesList(generic.ListView):
    model = Badge
    context_object_name = 'all_badges'
    template_name = 'badges/badges_list.html'
    paginate_by = 10