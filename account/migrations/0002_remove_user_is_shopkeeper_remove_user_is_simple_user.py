# Generated by Django 4.2.3 on 2024-11-10 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_shopkeeper",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_simple_user",
        ),
    ]