# Generated by Django 3.2.3 on 2021-06-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('doc_pk', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('doc_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('doc_type', models.SmallIntegerField(choices=[(0, 'Generic'), (1, 'Passport')], default=0)),
                ('owner_id', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
