# Generated by Django 4.2.2 on 2023-07-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0014_employee_employee_user_personal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_user_personal_id',
            field=models.CharField(default=None, editable=False, max_length=6, null=True, unique=True),
        ),
    ]