# Generated by Django 4.2.10 on 2024-07-25 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_alter_project_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
    ]
