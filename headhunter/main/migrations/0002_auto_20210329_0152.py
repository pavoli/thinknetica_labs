# Generated by Django 3.1.7 on 2021-03-29 01:52
import datetime

from django.db import migrations, models


def set_my_defaults(apps, schema_editor):
    Employer = apps.get_model('main', 'Employer')
    for emp in Employer.objects.all():
        emp.update_date = datetime.now()
        emp.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='Employer',
            name='update_date',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.RunPython(set_my_defaults),
        migrations.AlterField(
            model_name='Employer',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]