# Generated by Django 4.2.3 on 2024-11-30 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Library", "0006_alter_book_category_alter_book_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="Borrowingbook",
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
                (
                    "expiration_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="تاریخ انقضا"
                    ),
                ),
                (
                    "date_added",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ تولید"),
                ),
                (
                    "book",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="rents",
                        to="Library.book",
                        verbose_name="کتاب",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rents",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربر",
                    ),
                ),
            ],
            options={
                "verbose_name": "امانت",
                "verbose_name_plural": "امانت ها ",
                "ordering": ("-date_added",),
            },
        ),
    ]