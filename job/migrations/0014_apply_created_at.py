# Generated by Django 4.2.5 on 2023-09-13 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_alter_job_cetegory'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]