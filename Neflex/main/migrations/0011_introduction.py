# Generated by Django 3.2.6 on 2021-11-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_emotion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.FloatField()),
                ('Director', models.CharField(max_length=100)),
                ('Actor_list', models.CharField(max_length=100)),
            ],
        ),
    ]
