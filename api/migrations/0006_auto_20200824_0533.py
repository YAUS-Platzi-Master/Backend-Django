# Generated by Django 3.1 on 2020-08-24 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20200824_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seturl',
            name='user_id',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='set_url', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='auth.user'),
            preserve_default=False,
        ),
    ]
