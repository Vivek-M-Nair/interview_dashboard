# Generated by Django 5.1.6 on 2025-03-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0002_rename_index_contact_for'),
    ]

    operations = [
        migrations.CreateModel(
            name='cont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='contact_for',
        ),
    ]
