# Generated by Django 2.2 on 2019-06-29 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_auto_20190623_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='topping',
        ),
        migrations.AddField(
            model_name='orderline',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='itemId',
            field=models.ManyToManyField(blank=True, related_name='orderItems', to='menu.Item'),
        ),
        migrations.CreateModel(
            name='OrderLineTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderLineId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toppings', to='menu.OrderLine')),
                ('topping', models.ManyToManyField(blank=True, related_name='orderToppings', to='menu.Topping')),
            ],
        ),
    ]