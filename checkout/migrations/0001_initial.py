# Generated by Django 3.2.10 on 2022-01-06 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0011_auto_20211228_0932"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_number", models.CharField(max_length=254)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("net_total", models.IntegerField()),
                ("vat", models.IntegerField()),
                ("gross_total", models.IntegerField()),
            ],
            options={
                "verbose_name_plural": "Orders",
            },
        ),
        migrations.CreateModel(
            name="OrderLineItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(default=0)),
                (
                    "lineitem_total",
                    models.DecimalField(decimal_places=2, editable=False, max_digits=6),
                ),
                ("lineItem_vat", models.IntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lineitems",
                        to="checkout.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
