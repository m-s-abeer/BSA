from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from .models import Announcement
from .forms import AnnouncementForm


class AddAnnouncement(TemplateView):
    template_name = 'announcement/add.html'

    def get(self, request, *args, **kwargs):
        form = AnnouncementForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AnnouncementForm(request.POST)

        if form.is_valid():
            model = form.save(commit=False)
            model.author = request.user
            model.save()
            messages.success(request, 'Announcement Published.', fail_silently=True)
            return HttpResponseRedirect(reverse('announcement:add_announcement'))
        else:
            return render(request, self.template_name, {'form': form})
