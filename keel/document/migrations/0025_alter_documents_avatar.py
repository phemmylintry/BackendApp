# Generated by Django 3.2.3 on 2021-08-20 08:21

from django.db import migrations, models
import keel.Core.storage_backends
import keel.document.utils


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0024_alter_documents_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='avatar',
            field=models.FileField(blank=True, storage=keel.Core.storage_backends.PrivateMediaStorage(), upload_to=keel.document.utils.upload_files_to, verbose_name='Documents'),
        ),
    ]
