# Generated by Django 3.2.6 on 2021-11-04 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_like_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='like_movie',
        ),
    ]
