# Generated by Django 4.2.3 on 2024-11-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_alter_user_is_superuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name=" ایمیل"
            ),
        ),
    ]
