# Generated by Django 4.2.3 on 2024-11-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Library", "0007_borrowingbook"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="browssing",
            field=models.BooleanField(default=False, verbose_name="امانت"),
        ),
    ]
