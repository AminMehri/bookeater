# Generated by Django 3.2.10 on 2022-09-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_comment_comments_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comments_reply',
            field=models.ManyToManyField(blank=True, to='api.Comment'),
        ),
    ]
