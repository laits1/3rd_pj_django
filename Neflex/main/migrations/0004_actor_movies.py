# Generated by Django 3.2.6 on 2021-11-08 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211102_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(to='main.Movies'),
        ),
    ]
