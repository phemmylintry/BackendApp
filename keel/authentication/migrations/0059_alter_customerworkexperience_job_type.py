# Generated by Django 3.2.3 on 2021-08-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0058_auto_20210820_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerworkexperience',
            name='job_type',
            field=models.CharField(blank=True, default=None, max_length=512, null=True),
        ),
    ]
