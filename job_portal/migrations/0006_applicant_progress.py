# Generated by Django 4.0.1 on 2022-03-01 09:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0005_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='progress',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
