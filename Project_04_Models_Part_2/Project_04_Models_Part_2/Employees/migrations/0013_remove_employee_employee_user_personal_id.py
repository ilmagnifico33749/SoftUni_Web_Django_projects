# Generated by Django 4.2.2 on 2023-07-17 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0012_employee_employee_user_personal_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_user_personal_id',
        ),
    ]
