# Generated by Django 3.1.7 on 2021-04-01 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210329_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='skill',
            field=models.ManyToManyField(
                help_text='Select a skill for Candidate',
                 to='main.Technology'),
        ),
    ]
