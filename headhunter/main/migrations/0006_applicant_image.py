# Generated by Django 3.1.7 on 2021-04-10 15:00
from django.db import migrations

import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210409_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='image',
            field=sorl.thumbnail.fields.ImageField(
                blank=True,
                 null=True,
                upload_to='images'),
        ),
    ]
