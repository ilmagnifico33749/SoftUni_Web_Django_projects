# Generated by Django 4.2.2 on 2023-07-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0023_alter_employee_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_photo',
            field=models.ImageField(blank=True, null=True, upload_to='employee_user_photos/<django.db.models.fields.CharField>/<django.db.models.fields.SlugField>', verbose_name='Employee photo'),
        ),
    ]