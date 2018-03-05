from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Sheet, SheetMember

# Create your views here.
class ListSheets(generic.ListView):
    model = Sheet
    context_object_name = 'sheets_list'
    template_name = 'sheets/sheet_list.html'

class SheetView(TemplateView):
    template_name = 'sheets/sheet_detail.html'
