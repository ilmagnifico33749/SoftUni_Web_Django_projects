# Generated by Django 4.2.2 on 2023-06-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.CharField(max_length=10, unique=True, verbose_name='Department ID')),
                ('department_name', models.CharField(max_length=30, unique=True, verbose_name='Department name')),
                ('department_employees_id', models.CharField(max_length=10, unique=True, verbose_name='Employee ID')),
                ('department_email_address', models.EmailField(max_length=254, verbose_name='Department email address')),
                ('department_project_id', models.CharField(max_length=300, verbose_name='Involved in Projects')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=10, unique=True, verbose_name='Employee ID')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=40, verbose_name='Last name')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('department_name', models.CharField(max_length=30, verbose_name='Department name')),
                ('department_id', models.CharField(max_length=10, unique=True, verbose_name='Department ID')),
                ('project_id', models.CharField(max_length=300, verbose_name='Involved in Projects')),
                ('seniority', models.CharField(max_length=20, verbose_name='Seniority')),
                ('position', models.CharField(max_length=30)),
                ('employee_email_address', models.EmailField(max_length=30, unique=True, verbose_name='Employee email address')),
                ('employed_permanently', models.BooleanField(blank=True, verbose_name='Employed permanently')),
                ('employed_on_probation', models.BooleanField(blank=True, verbose_name='On probation')),
                ('employed_full_time', models.BooleanField(blank=True, verbose_name='Employed full time')),
                ('photo', models.URLField(blank=True, max_length=100, verbose_name='Photo')),
                ('birth_date', models.DateField(blank=True, verbose_name='Birth date')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(blank=True, max_length=10, unique=True, verbose_name='Project ID')),
                ('project_name', models.CharField(max_length=30, unique=True, verbose_name='Project name')),
                ('project_department_id', models.CharField(blank=True, max_length=300, verbose_name='Departments involved')),
                ('project_employees_id', models.CharField(blank=True, max_length=300, verbose_name='Employees involved')),
                ('project_status', models.BooleanField(blank=True, choices=[('Planing', 'Planing'), ('Development', 'Development'), ('Deployed', 'Deployed')], max_length=50, verbose_name='Project status')),
                ('project_email_address', models.EmailField(max_length=254, verbose_name='Project email address')),
            ],
        ),
    ]