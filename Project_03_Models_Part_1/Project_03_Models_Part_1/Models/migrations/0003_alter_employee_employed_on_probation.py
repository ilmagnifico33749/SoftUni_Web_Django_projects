# Generated by Django 4.2.2 on 2023-06-19 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0002_alter_employee_employed_permanently'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employed_on_probation',
            field=models.BooleanField(choices=[('True', 'True'), ('False', 'False')], verbose_name='On probation'),
        ),
    ]
