# Generated by Django 3.2.18 on 2023-04-17 10:56

import appone.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0007_remove_uploadmatch_name_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadmatch',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=appone.models.get_upload_path),
        ),
    ]
