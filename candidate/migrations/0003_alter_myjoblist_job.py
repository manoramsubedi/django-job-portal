# Generated by Django 5.1.3 on 2024-12-01 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_alter_myjoblist_user'),
        ('hr', '0003_alter_candidateapplication_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myjoblist',
            name='job',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hr.candidateapplication'),
        ),
    ]