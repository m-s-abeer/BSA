from django.shortcuts import render, get_object_or_404
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
