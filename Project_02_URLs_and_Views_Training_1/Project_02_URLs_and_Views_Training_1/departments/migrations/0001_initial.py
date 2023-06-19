# Generated by Django 4.2.1 on 2023-05-31 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=30)),
                ('department_id', models.CharField(max_length=30)),
                ('department_philosophy_id', models.CharField(max_length=100)),
                ('department_size', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_member_name', models.CharField(max_length=30)),
                ('employee_member_position', models.CharField(max_length=30)),
                ('employee_member_personal_id', models.CharField(max_length=2)),
                ('employee_member_department_id', models.CharField(max_length=2)),
                ('employee_member_languages_and_frameworks_used', models.CharField(max_length=50)),
                ('employee_philosophy_id', models.CharField(max_length=100)),
                ('employee_member_working_on_projects_num', models.CharField(max_length=30)),
                ('employee_member_working_on_projects_by_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Philosophy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('philosophy_name', models.CharField(max_length=100)),
                ('philosophy_id', models.CharField(max_length=100)),
                ('philosophy_description', models.CharField(max_length=100)),
                ('philosophy_department_following_num', models.CharField(max_length=100)),
                ('philosophy_department_following_by_id', models.CharField(max_length=100)),
                ('philosophy_department_following_by_name', models.CharField(max_length=100)),
                ('philosophy_employees_following_num', models.CharField(max_length=100)),
                ('philosophy_employees_following_by_id', models.CharField(max_length=100)),
                ('philosophy_employees_following_by_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=2)),
                ('project_name', models.CharField(max_length=30)),
                ('project_languages_and_frameworks_used', models.CharField(max_length=50)),
                ('project_involved_departments_num', models.CharField(max_length=30)),
                ('project_involved_departments_by_id', models.CharField(max_length=30)),
                ('project_involved_departments_by_name', models.CharField(max_length=50)),
                ('project_involved_employees_by_num', models.CharField(max_length=30)),
                ('project_involved_employees_by_id', models.CharField(max_length=30)),
                ('project_involved_employees_by_name', models.CharField(max_length=50)),
            ],
        ),
    ]