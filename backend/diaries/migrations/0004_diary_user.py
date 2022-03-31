# Generated by Django 3.2.12 on 2022-03-15 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diaries', '0003_auto_20220310_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='diaries', to='accounts.user'),
            preserve_default=False,
        ),
    ]