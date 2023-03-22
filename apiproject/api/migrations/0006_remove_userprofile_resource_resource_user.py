# Generated by Django 4.1.7 on 2023-03-22 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_post_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='resource',
        ),
        migrations.AddField(
            model_name='resource',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
