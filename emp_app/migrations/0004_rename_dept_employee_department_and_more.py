# Generated by Django 5.2 on 2025-05-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0003_auto_20250510_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='dept',
            new_name='department',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phone',
        ),
        migrations.AddField(
            model_name='employee',
            name='location',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='bonus',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
