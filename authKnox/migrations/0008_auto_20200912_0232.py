# Generated by Django 3.1 on 2020-09-12 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authKnox', '0007_auto_20200829_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokenprofile',
            name='user_agent',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
