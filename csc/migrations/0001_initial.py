# Generated by Django 4.2.7 on 2024-09-21 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'db_table': 'country',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='Name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csc.country', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
                'db_table': 'state',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='Name')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csc.state', verbose_name='State')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'db_table': 'city',
                'managed': True,
            },
        ),
    ]