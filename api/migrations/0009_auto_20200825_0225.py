# Generated by Django 3.1 on 2020-08-25 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200825_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seturl',
            name='deleted',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
