from django.shortcuts import render
from django.views import generic
from .models import Problem

# Create your views here.

class ProblemList(generic.ListView):
    model = Problem
    context_object_name = 'all_problems'
    template_name = 'problems/problem_list.html'

class ProblemDetail(generic.DetailView):
    model = Problem
    template_name = 'problems/problem_detail.html'
