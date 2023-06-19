# Generated by Django 4.2.2 on 2023-06-19 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0010_project_employees_appointment_test_department_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project_employees_appointment',
            old_name='employee',
            new_name='test_employee',
        ),
        migrations.RenameField(
            model_name='project_employees_appointment',
            old_name='project',
            new_name='test_project',
        ),
        migrations.RenameField(
            model_name='project_employees_appointment',
            old_name='role',
            new_name='test_role',
        ),
        migrations.RenameField(
            model_name='project_employees_appointment',
            old_name='start_date',
            new_name='test_start_date',
        ),
        migrations.RenameField(
            model_name='test_department_employees_appointment',
            old_name='department',
            new_name='test_department',
        ),
        migrations.RenameField(
            model_name='test_department_employees_appointment',
            old_name='employees',
            new_name='test_department_employees',
        ),
        migrations.RenameField(
            model_name='test_department_employees_appointment',
            old_name='role',
            new_name='test_role',
        ),
        migrations.RenameField(
            model_name='test_department_employees_appointment',
            old_name='start_date',
            new_name='test_start_date',
        ),
        migrations.AlterField(
            model_name='test_employee',
            name='test_employee_full_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='TEST_Full name'),
        ),
        migrations.AlterField(
            model_name='test_employee',
            name='test_employee_id',
            field=models.CharField(max_length=10, unique=True, verbose_name='TEST_Employee ID'),
        ),
    ]
