# Generated by Django 3.1.5 on 2021-03-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_product_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_state',
            field=models.BooleanField(verbose_name='Состояние готовности продукта'),
        ),
    ]
