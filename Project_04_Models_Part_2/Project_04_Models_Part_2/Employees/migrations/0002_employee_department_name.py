# Generated by Django 4.2.2 on 2023-06-28 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Departments', '0001_initial'),
        ('Employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Departments.department'),
        ),
    ]
