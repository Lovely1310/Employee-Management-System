# Generated by Django 5.2 on 2025-05-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0004_rename_dept_employee_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=10),
        ),
    ]
