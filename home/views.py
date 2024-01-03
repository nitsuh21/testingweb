# test_automation_app/views.py

from django.shortcuts import render, redirect
from .forms import TestCaseForm
from .models import TestCase
from scripts.cbe.cbe_login_test import runtest

def home(request):
    form = TestCaseForm()
    return render(request, 'home.html', {'form': form})

def select(request):
    if request.method == 'POST':
        form = TestCaseForm(request.POST)
        if form.is_valid():
            test_case = form.save()
            # Check if the button for running the test was clicked
            #call the runtest function
            if 'run_test_button' in request.POST:
                runtest(test_case)  # Trigger Selenium test
            return redirect('test_results')
    else:
        return redirect('home')