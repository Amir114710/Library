# Generated by Django 4.2.3 on 2024-11-10 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_remove_user_is_shopkeeper_remove_user_is_simple_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False, verbose_name=" سوپر یوزر"),
        ),
    ]