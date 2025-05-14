import django.db.models.deletion
from django.db import migrations, models

def set_defaults(apps, schema_editor):
    Employee = apps.get_model('emp_app', 'Employee')  # Replace 'emp_app' with your actual app name if needed
    for emp in Employee.objects.all():
        if not emp.phone_number:
            emp.phone_number = '0000000000'
        if not emp.location:
            emp.location = 'Unknown'
        emp.save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # Add previous migration dependencies if applicable, e.g.:
        # ('emp_app', 'previous_migration_name'),
    ]

    operations = [
        # Create the 'Role' model
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        # Create the 'Employee' model
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('salary', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('phone_number', models.CharField(max_length=10, default='0000000000')),  # Corrected the field name
                ('hire_date', models.DateField()),
                ('location', models.CharField(max_length=100, default='Unknown')),  # Added 'location' with a default
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.department')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.role')),
            ],
        ),
        # Set default values for the existing records (this will run after the models are created)
        migrations.RunPython(set_defaults),
        # Alter the 'phone_number' and 'location' fields to make them non-nullable
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
