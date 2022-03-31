# Generated by Django 3.2.12 on 2022-03-27 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0012_alter_flower_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='custom_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='diary',
            name='flower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diaries', to='diaries.flower'),
        ),
    ]