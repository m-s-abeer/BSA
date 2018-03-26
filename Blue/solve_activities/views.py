from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from problems.models import Problem
from .models import Solve
from sheets.models import SheetMember
# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()

class SolveConfirmation(LoginRequiredMixin, generic.TemplateView):
    template_name = 'solve_activities/solve_confirmation.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["prob"] = get_object_or_404(Problem, slug=kwargs['slug'])
        context["solve_status"] = self.request.user.is_authenticated and context["prob"].solved.filter(solver=self.request.user).exists()
        return context

    def post(self, request, *args, **kwargs):
        problem = get_object_or_404(Problem, slug=kwargs['slug'])
        Solve.objects.create(problem=problem, solver=request.user)
        sheet_mem=SheetMember.objects.filter(member=request.user)
        ## If the user is a member of any sheet, it'll update the solve count of him in that sheet
        if sheet_mem:
            sheet_mem=sheet_mem[0]
            isPos = problem in Problem.objects.order_by("created_at")[0:sheet_mem.sheet.problems_added]
            if isPos:
                sheet_mem.solve_count = sheet_mem.solve_count + 1
                sheet_mem.save()
        success_msg="<h1><b>Congratulations! You've solved \"" + str(problem) + "\".</b></h1>"
        return HttpResponse(success_msg)
