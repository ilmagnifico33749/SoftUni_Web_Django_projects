# Generated by Django 4.2.2 on 2023-07-18 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0016_employee_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_slug',
        ),
    ]
