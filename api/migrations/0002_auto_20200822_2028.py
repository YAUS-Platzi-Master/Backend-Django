# Generated by Django 3.1 on 2020-08-22 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seturl',
            name='long_url',
            field=models.URLField(),
        ),
    ]
