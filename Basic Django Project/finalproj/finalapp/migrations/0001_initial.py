# Generated by Django 5.0.6 on 2024-07-06 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('uid', models.IntegerField(default=1001, editable=False, primary_key=True, serialize=False, unique=True)),
                ('mail', models.CharField(default='faculty@example.com', max_length=40, unique=True)),
                ('password', models.CharField(default='temporary_password', max_length=50)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('uid', models.IntegerField(default=101, editable=False, primary_key=True, serialize=False, unique=True)),
                ('mail', models.CharField(default='parent@example.com', max_length=40, unique=True)),
                ('password', models.CharField(default='temporary_password', max_length=50)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('sender_uid', models.IntegerField(default=0)),
                ('receiver_uid', models.IntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uid', models.IntegerField(default=10, editable=False, primary_key=True, serialize=False, unique=True)),
                ('mail', models.CharField(default='student@example.com', max_length=40, unique=True)),
                ('password', models.CharField(default='temporary_password', max_length=50)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=50, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finalapp.parent')),
            ],
        ),
    ]
