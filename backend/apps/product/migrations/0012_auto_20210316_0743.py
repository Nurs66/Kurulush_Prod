# Generated by Django 3.1.5 on 2021-03-16 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_technicaldata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicaldata',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='technical_data', to='product.product', verbose_name='Продукт'),
        ),
    ]
