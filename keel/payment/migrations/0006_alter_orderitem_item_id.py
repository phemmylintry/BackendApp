# Generated by Django 3.2.3 on 2021-10-12 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_auto_20210918_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='item_id',
            field=models.CharField(max_length=512),
        ),
    ]
