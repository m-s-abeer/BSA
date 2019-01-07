from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.

class Register(CreateView):
    template_name = 'profiles/register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('login')
