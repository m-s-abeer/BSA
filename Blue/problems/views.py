from django.shortcuts import render
from django.views import generic
from .models import Problem
from solve_activities.models import Solve

# Create your views here.

class ProblemList(generic.ListView):
    model = Problem
    context_object_name = 'all_problems'
    template_name = 'problems/problem_list.html'

class ProblemDetail(generic.DetailView):
    model = Problem
    template_name = 'problems/problem_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # slower: context["solved_status"] = self.request.user.is_authenticated and Solve.objects.filter(solver=self.request.user, problem=context["object"]).exists()
        context["solve_status"] = self.request.user.is_authenticated and context["object"].solved.filter(solver=self.request.user).exists()
        context['current_url'] = self.request.get_full_path()
<<<<<<< HEAD
        context['active_tab'] = 'problems'
=======
>>>>>>> Sheet-View-and-Popup-upda
        return context
