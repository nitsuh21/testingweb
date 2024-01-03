# test_automation_app/views.py

from django.shortcuts import render, redirect
from .forms import TestCaseForm
from .models import TestCase
from scripts.cbe.cbe_login_test import run_selenium_test

def home(request):
    if request.method == 'POST':
        form = TestCaseForm(request.POST)
        if form.is_valid():
            test_case = form.save()
            run_selenium_test(test_case)
            return redirect('test_results')
    else:
        form = TestCaseForm()
    
    return render(request, 'home.html', {'form': form})

def test_results(request):
    test_cases = TestCase.objects.all()
    return render(request, 'test_results.html', {'test_cases': test_cases})
