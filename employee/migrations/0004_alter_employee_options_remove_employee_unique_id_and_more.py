# Generated by Django 5.1.1 on 2024-09-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_unique_id_alter_employee_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='unique_id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
    ]
