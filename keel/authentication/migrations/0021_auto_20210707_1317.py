# Generated by Django 3.2.3 on 2021-07-07 07:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0020_alter_passwordresettoken_expiry_date'),
    ]

    operations = [
        # migrations.RenameField(
        #     model_name='user',
        #     old_name='uuid',
        #     new_name='id',
        # ),
        # migrations.AlterField(
        #     model_name='passwordresettoken',
        #     name='expiry_date',
        #     field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 7, 57, 53, 369365, tzinfo=utc)),
        # ),
    ]
