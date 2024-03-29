# Generated by Django 5.0.3 on 2024-03-29 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('born_date', models.CharField(max_length=35)),
                ('born_location', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=3500)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=700)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quoteapp.author')),
            ],
        ),
    ]