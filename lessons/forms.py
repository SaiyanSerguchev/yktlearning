from django import forms
from .models import *


class LessonDone(forms.ModelForm):
    done = forms.BooleanField(widget=forms.HiddenInput(), initial=True)

    class Meta:
        model = DoneLessonsModel
        fields =['done']