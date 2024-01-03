# test_report/models.py

from django.db import models

class TestCase(models.Model):
    test_name = models.CharField(max_length=255)
    website_link = models.URLField()
    status = models.CharField(max_length=20)
    details = models.TextField()
    screenshot_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.test_name

class Test(models.Model):
    test_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    log = models.TextField()
    rate = models.FloatField()
    screenshot_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.test_name