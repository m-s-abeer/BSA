from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from django.db.models import Q
from announcement.models import Announcement
from .models import Sheet, SheetMember
from problems.models import Problem
import json

# Create your views here.
class ListSheets(generic.ListView):
    model = Sheet
    context_object_name = 'sheets_list'
    template_name = 'sheets/sheet_list.html'


class SheetView(TemplateView):
    template_name = 'sheets/main_sheet.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        this_sheet = context['this_sheet'] = get_object_or_404(Sheet, slug=kwargs['slug'])
        lim = context['this_sheet'].problems_added
        context['sheet_prob'] = Problem.objects.order_by("created_at")[0:lim]
        context['sheet_status'] = self.request.user.is_authenticated and SheetMember.objects.filter(
            member=self.request.user).exists()
        context['member_list'] = context['this_sheet'].memberships.order_by("-solve_count")
        context['announcements'] = Announcement.objects.filter(Q(sheets=this_sheet) | Q(sheets=None))
        context['current_url'] = self.request.get_full_path()
        return context


class JoinSheetView(TemplateView):
    template_name = 'sheets/join_sheet_confirmation.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['this_sheet'] = get_object_or_404(Sheet, slug=kwargs['slug'])
        context['member_status'] = self.request.user.is_authenticated and context['this_sheet'].memberships.filter(
            member=self.request.user).exists()
        cnt = sheet_solve_count(context['this_sheet'], self.request.user)
        context['solve_count'] = cnt
        context['eligible'] = cnt >= context['this_sheet'].cut_off
        return context

    def post(self, request, *args, **kwargs):
        sheet = get_object_or_404(Sheet, slug=kwargs['slug'])
        lim = sheet.cut_off
        cnt = sheet_solve_count(sheet, self.request.user)
        if cnt >= lim:
            SheetMember.objects.create(sheet=sheet, member=self.request.user, solve_count=cnt)
            success_msg = "<h1><b>Congratulations! You've joined \"" + str(sheet) + "\".</b></h1>"
            return HttpResponse(success_msg)
        else:
            failed_msg = "<h1><b>Some error occured while joining \"" + str(sheet) + "\".</b></h1>"
            return HttpResponse(failed_msg)


# Methods
def sheet_solve_count(sheet, user):
    lim = sheet.problems_added
    sheet_probs = Problem.objects.order_by("created_at")[0:lim]
    cnt = int(0)
    for prob in sheet_probs:
        if prob.solved.filter(solver=user).exists() == 1:
            cnt = cnt + 1
    return cnt


@login_required
def xhr_sheet_join(request, slug):
    sheet = get_object_or_404(Sheet, slug=slug)
    lim = sheet.cut_off
    cnt = sheet_solve_count(sheet, request.user)
    if cnt >= lim:
        SheetMember.objects.create(sheet=sheet, member=request.user, solve_count=cnt)
        response = {
            'status': 1,
            'message': "<h1><b>Congratulations! You've joined \"" + str(sheet) + "\".</b></h1>"
        }
    else:
        response = {
            'status': 0,
            'message': "<h1><b>Some error occured while joining \"" + str(sheet) + "\".</b></h1>"
        }

    return HttpResponse(json.dumps(response))
