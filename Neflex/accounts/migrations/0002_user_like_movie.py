# Generated by Django 3.2.6 on 2021-11-02 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_movie',
            field=models.TextField(blank=True),
        ),
    ]
