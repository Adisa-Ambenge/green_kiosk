# Generated by Django 4.2.4 on 2023-08-12 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('cart', '0005_cart_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
    ]
