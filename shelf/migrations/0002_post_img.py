# Generated by Django 3.0.2 on 2020-01-14 22:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]