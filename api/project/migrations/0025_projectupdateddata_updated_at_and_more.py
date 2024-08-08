# Generated by Django 4.2.10 on 2024-08-05 08:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_department_company'),
        ('project', '0024_remove_projectupdateddata_project_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectupdateddata',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectupdateddata',
            name='updated_by',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_projects_by', to='user.userrole'),
            preserve_default=False,
        ),
    ]
