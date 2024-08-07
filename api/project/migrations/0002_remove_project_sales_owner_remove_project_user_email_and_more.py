# Generated by Django 4.2.10 on 2024-07-12 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='sales_owner',
        ),
        migrations.RemoveField(
            model_name='project',
            name='user_email',
        ),
        migrations.AddField(
            model_name='project',
            name='initial_sample_size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Hold', 'Hold')], default='Pending', max_length=20),
        ),
    ]
