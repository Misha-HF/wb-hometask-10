# Generated by Django 5.0.3 on 2024-03-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0003_alter_author_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
