# Generated by Django 3.1 on 2020-10-21 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opakowania', '0024_position_activeproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='deletedProducts',
            field=models.PositiveIntegerField(default=0),
        ),
    ]