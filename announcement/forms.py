from .models import Announcement
from django import forms
from sheets.models import Sheet


class AnnouncementForm(forms.ModelForm):
    title = forms.CharField(max_length=5000, min_length=5, required=True)
    content = forms.CharField(max_length=5000, min_length=5, widget=forms.Textarea)
    sheets = forms.ModelChoiceField(Sheet.objects.all(), required=False, empty_label='All Sheets')

    class Meta:
        model = Announcement
        fields = ['title', 'content', 'sheets']
