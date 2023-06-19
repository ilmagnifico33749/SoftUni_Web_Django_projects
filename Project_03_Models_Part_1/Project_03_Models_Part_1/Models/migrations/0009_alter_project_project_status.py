# Generated by Django 4.2.2 on 2023-06-19 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0008_alter_project_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(choices=[('Planing', 'Planing'), ('Development', 'Development'), ('Deployed', 'Deployed'), ('N/A', 'N/A')], default='N/A', max_length=50, verbose_name='Project status'),
        ),
    ]
