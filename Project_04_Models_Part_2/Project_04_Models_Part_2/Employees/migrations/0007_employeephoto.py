# Generated by Django 4.2.2 on 2023-07-15 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0006_employee_employee_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_photo', models.ImageField(upload_to='employee_user_photos')),
            ],
        ),
    ]
