from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from .models import Sheet, SheetMember
from problems.models import Problem

# Create your views here.
class ListSheets(generic.ListView):
    model = Sheet
    context_object_name = 'sheets_list'
    template_name = 'sheets/sheet_list.html'

class SheetView(TemplateView):
    template_name = 'sheets/main_sheet.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['this_sheet'] = get_object_or_404(Sheet, slug=kwargs['slug'])
        lim = context['this_sheet'].problem_count
        context['sheet_prob'] = Problem.objects.order_by("created_at")[0:lim]
        context['sheet_status'] = self.request.user.is_authenticated and SheetMember.objects.filter(user=self.request.user).exists()
        context['member_list'] = context['this_sheet'].memberships.order_by("-solve_count")
        return context

class JoinSheetView(TemplateView):
    template_name = 'sheets/join_sheet_confirmation.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['this_sheet'] = get_object_or_404(Sheet, slug=kwargs['slug'])
        context['member_status'] = self.request.user.is_authenticated and context['this_sheet'].memberships.filter(user=self.request.user).exists()
        cnt = sheet_solve_count(context['this_sheet'], self.request.user)
        context['solve_count'] = cnt
        context['eligible'] = cnt >= context['this_sheet'].problem_count
        return context

    def post(self, request, *args, **kwargs):
        sheet = get_object_or_404(Sheet, slug=kwargs['slug'])
        lim = sheet.problem_count
        cnt = sheet_solve_count(sheet, self.request.user)
        if cnt >= lim :
            SheetMember.objects.create(sheet=sheet, user=self.request.user, solve_count=cnt)
            success_msg="<h1><b>Congratulations! You've joined \"" + str(sheet) + "\".</b></h1>"
            return HttpResponse(success_msg)
        else:
            failed_msg="<h1><b>Some error occured while joining \"" + str(sheet) + "\".</b></h1>"
            return HttpResponse(failed_msg)

# Methods
def sheet_solve_count(sheet, user):
    lim = sheet.problem_count
    sheet_probs = Problem.objects.order_by("created_at")[0:lim]
    cnt = int(0)
    for prob in sheet_probs:
        if prob.solved.filter(solver=user).exists() == 1:
            cnt = cnt + 1
    return cnt
