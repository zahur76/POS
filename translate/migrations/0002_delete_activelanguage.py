# Generated by Django 3.2.10 on 2021-12-25 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("translate", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="activeLanguage",
        ),
    ]
