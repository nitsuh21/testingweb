# Generated by Django 5.0.1 on 2024-01-03 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=20)),
                ('log', models.TextField()),
                ('rate', models.FloatField()),
                ('screenshot_path', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=255)),
                ('website_link', models.URLField()),
                ('status', models.CharField(max_length=20)),
                ('details', models.TextField()),
                ('screenshot_path', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TestRun',
        ),
    ]