# Generated by Django 4.0.5 on 2022-07-14 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, verbose_name='Nome')),
                ('description', models.CharField(blank=True, max_length=512, verbose_name='Descrição')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.company')),
            ],
        ),
    ]
