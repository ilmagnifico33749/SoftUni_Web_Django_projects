# Generated by Django 4.2.2 on 2023-06-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0007_alter_employee_employed_full_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.BooleanField(blank=True, choices=[('Planing', 'Planing'), ('Development', 'Development'), ('Deployed', 'Deployed')], max_length=50, null=True, verbose_name='Project status'),
        ),
    ]
