# Generated by Django 4.2.3 on 2024-11-06 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Library", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={
                "ordering": ("-created",),
                "verbose_name": "کتاب",
                "verbose_name_plural": "کتاب ها ",
            },
        ),
        migrations.AddField(
            model_name="book",
            name="status",
            field=models.BooleanField(default=True, verbose_name="موجودی"),
        ),
        migrations.AlterField(
            model_name="book",
            name="type",
            field=models.ManyToManyField(
                null=True,
                related_name="books_type",
                to="Library.type",
                verbose_name="نوع کتاب",
            ),
        ),
    ]
