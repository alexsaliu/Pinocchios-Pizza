# Generated by Django 2.2 on 2019-06-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20190609_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sizes',
            field=models.BooleanField(default=False),
        ),
    ]
