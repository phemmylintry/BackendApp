# Generated by Django 3.2.3 on 2021-10-19 10:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0003_alter_quotation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotationmilestone',
            name='qm_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False),
        ),
    ]
