# test_automation_app/forms.py

from django import forms
from .models import TestCase

class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ['website_link', 'test_name']
