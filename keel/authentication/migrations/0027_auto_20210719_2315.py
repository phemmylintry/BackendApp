# Generated by Django 3.2.3 on 2021-07-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0026_merge_20210714_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdocument',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='userservice',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
