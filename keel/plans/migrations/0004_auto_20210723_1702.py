# Generated by Django 3.2.3 on 2021-07-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0003_service_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
