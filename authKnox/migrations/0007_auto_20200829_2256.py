# Generated by Django 3.1 on 2020-08-29 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authKnox', '0006_auto_20200829_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokenprofile',
            name='Cookie',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
