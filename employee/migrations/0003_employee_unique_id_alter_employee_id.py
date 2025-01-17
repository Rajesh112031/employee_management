# Generated by Django 5.1.1 on 2024-09-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_options_alter_employee_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='unique_id',
            field=models.CharField(default=0, editable=False, max_length=4, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
