# Generated by Django 4.2.2 on 2023-06-28 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0002_alter_project_project_name'),
        ('Employees', '0002_employee_department_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='department_name',
            new_name='employee_department_name',
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_projects_involvement',
            field=models.ManyToManyField(to='Projects.project'),
        ),
    ]
