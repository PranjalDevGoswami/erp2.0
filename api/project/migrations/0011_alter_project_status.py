# Generated by Django 4.2.10 on 2024-07-25 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_delete_projectupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Project Initiated', 'Project Initiated'), ('To Be Started', 'To Be Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('On Hold', 'On Hold')], default='To Be Started', max_length=20),
        ),
    ]
