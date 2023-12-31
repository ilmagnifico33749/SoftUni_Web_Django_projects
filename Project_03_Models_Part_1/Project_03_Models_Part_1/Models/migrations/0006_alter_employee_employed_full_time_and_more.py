# Generated by Django 4.2.2 on 2023-06-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0005_alter_employee_employed_on_probation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employed_full_time',
            field=models.BooleanField(blank=True, verbose_name='Employed full time'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employed_on_probation',
            field=models.BooleanField(blank=True, null=True, verbose_name='On probation'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employed_permanently',
            field=models.BooleanField(blank=True, verbose_name='Employed permanently'),
        ),
    ]
