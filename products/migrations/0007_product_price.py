# Generated by Django 3.2.10 on 2021-12-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_alter_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.IntegerField(default=10, max_length=254),
        ),
    ]
