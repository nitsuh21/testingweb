# test_report/models.py

from django.db import models

class TestRun(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    test_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    details = models.TextField()
    screenshot_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.test_name