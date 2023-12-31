# Generated by Django 4.2.2 on 2023-06-19 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0009_alter_project_project_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Employees_Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('role', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Test_Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_department_id', models.CharField(max_length=10, unique=True, verbose_name='Department ID')),
                ('test_department_name', models.CharField(max_length=30, unique=True, verbose_name='Department name')),
                ('test_department_employees_id', models.CharField(max_length=10, unique=True, verbose_name='Employee ID')),
                ('test_department_email_address', models.EmailField(max_length=254, verbose_name='Department email address')),
                ('test_department_project_id', models.CharField(max_length=300, verbose_name='Involved in Projects')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Department_Employees_Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('role', models.CharField(max_length=30)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Models.test_department')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_project_id', models.CharField(blank=True, max_length=10, unique=True, verbose_name='Project ID')),
                ('test_project_name', models.CharField(max_length=30, unique=True, verbose_name='Project name')),
                ('test_project_department_id', models.CharField(blank=True, max_length=300, verbose_name='Departments involved')),
                ('test_project_employees_id', models.CharField(blank=True, max_length=300, verbose_name='Employees involved')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_employee_id', models.CharField(max_length=10, unique=True, verbose_name='Employee ID')),
                ('test_employee_full_name', models.CharField(blank=True, max_length=30, verbose_name='First name')),
                ('test_employee_department_appointment', models.ManyToManyField(through='Models.Test_Department_Employees_Appointment', to='Models.test_department')),
                ('test_employee_project_appointment', models.ManyToManyField(through='Models.Project_Employees_Appointment', to='Models.test_project')),
            ],
        ),
        migrations.AddField(
            model_name='test_department_employees_appointment',
            name='employees',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Models.test_employee'),
        ),
        migrations.AddField(
            model_name='project_employees_appointment',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Models.test_employee'),
        ),
        migrations.AddField(
            model_name='project_employees_appointment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Models.test_project'),
        ),
    ]
