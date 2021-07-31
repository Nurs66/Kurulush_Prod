# Generated by Django 3.1.5 on 2021-03-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210315_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_kg',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_kg',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_kg',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]
