# Generated by Django 3.1 on 2020-10-24 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opakowania', '0026_auto_20201021_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='orderNumberInPosition',
            field=models.IntegerField(default=1),
        ),
    ]
