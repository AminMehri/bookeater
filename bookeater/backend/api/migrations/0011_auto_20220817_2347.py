# Generated by Django 3.2.10 on 2022-08-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20220817_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/users'),
        ),
        migrations.AddField(
            model_name='user',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='media/users'),
        ),
    ]