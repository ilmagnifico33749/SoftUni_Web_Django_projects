# Generated by Django 4.2.2 on 2023-07-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0022_alter_employee_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='slug',
            field=models.SlugField(default=None),
        ),
    ]
