# Generated by Django 5.1.6 on 2025-03-12 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0010_alter_interviewprep_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewprep',
            name='domain',
            field=models.CharField(max_length=50),
        ),
    ]
