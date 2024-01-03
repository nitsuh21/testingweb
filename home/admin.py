from django.contrib import admin

# Register your models here.
from .models import TestCase, Test

admin.site.site_header = "Testing Automation Web Admin"

admin.site.register(TestCase)
admin.site.register(Test)
