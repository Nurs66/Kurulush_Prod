# Generated by Django 3.1.5 on 2021-03-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20210315_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='title_kg',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
