# Generated by Django 3.2.10 on 2022-01-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderlineitem",
            name="lineItem_vat",
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6),
        ),
    ]
