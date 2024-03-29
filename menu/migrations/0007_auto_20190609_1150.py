# Generated by Django 2.2 on 2019-06-09 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20190609_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoryToppings', to='menu.Category'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='item',
            field=models.ManyToManyField(blank=True, related_name='itemToppings', to='menu.Item'),
        ),
    ]
