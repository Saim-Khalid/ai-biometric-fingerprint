# Generated by Django 3.2.18 on 2023-03-15 09:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='user',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
