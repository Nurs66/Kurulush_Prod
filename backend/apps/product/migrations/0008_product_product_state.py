# Generated by Django 3.1.5 on 2021-03-15 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210315_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_state',
            field=models.BooleanField(default=1, verbose_name='Состояние продукта'),
            preserve_default=False,
        ),
    ]
