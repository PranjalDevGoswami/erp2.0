# Generated by Django 4.2.10 on 2024-07-30 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0006_alter_projectupdate_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectupdate',
            name='project',
        ),
    ]