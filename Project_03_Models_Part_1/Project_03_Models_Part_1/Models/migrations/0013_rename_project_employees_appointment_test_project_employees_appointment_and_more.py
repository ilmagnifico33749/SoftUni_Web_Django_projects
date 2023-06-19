# Generated by Django 4.2.2 on 2023-06-19 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0012_alter_test_department_test_department_email_address_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project_Employees_Appointment',
            new_name='Test_Project_Employees_Appointment',
        ),
        migrations.RemoveField(
            model_name='test_department_employees_appointment',
            name='test_department',
        ),
        migrations.RemoveField(
            model_name='test_department_employees_appointment',
            name='test_department_employees',
        ),
        migrations.RemoveField(
            model_name='test_employee',
            name='test_employee_department_appointment',
        ),
        migrations.RemoveField(
            model_name='test_project',
            name='test_project_department_id',
        ),
        migrations.DeleteModel(
            name='Test_Department',
        ),
        migrations.DeleteModel(
            name='Test_Department_Employees_Appointment',
        ),
    ]
