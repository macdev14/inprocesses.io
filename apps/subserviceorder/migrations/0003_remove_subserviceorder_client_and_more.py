# Generated by Django 4.0.5 on 2022-07-15 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subserviceorder', '0002_subserviceorder_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subserviceorder',
            name='client',
        ),
        migrations.AlterField(
            model_name='subserviceorder',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
