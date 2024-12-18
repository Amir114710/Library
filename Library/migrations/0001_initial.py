# Generated by Django 4.2.3 on 2024-11-05 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "title",
                    models.CharField(
                        max_length=250, null=True, verbose_name="نام دسته بندی"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "دسته بندی",
                "verbose_name_plural": "دسته بندی ها",
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="Leason",
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
                    "title",
                    models.CharField(max_length=350, null=True, verbose_name="نام درس"),
                ),
                ("created", models.DateField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "درس",
                "verbose_name_plural": "درس ها",
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="Type",
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
                    "title",
                    models.CharField(
                        max_length=350, null=True, verbose_name="نوع کتاب"
                    ),
                ),
                ("created", models.DateField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "نوع کتاب",
                "verbose_name_plural": "نوع کتاب ها",
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="Book",
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
                    "title",
                    models.CharField(
                        max_length=250, null=True, verbose_name="نام کتاب"
                    ),
                ),
                ("content", models.TextField(null=True, verbose_name="توضیحات")),
                (
                    "created_at",
                    models.IntegerField(null=True, verbose_name="سال انتشار"),
                ),
                (
                    "publisher",
                    models.CharField(max_length=450, null=True, verbose_name="ناشر"),
                ),
                ("the_author", models.TextField(null=True, verbose_name="مولفان")),
                (
                    "educational_base",
                    models.CharField(
                        max_length=350, null=True, verbose_name="پایه تحصیلی"
                    ),
                ),
                (
                    "image",
                    models.FileField(
                        null=True, upload_to="book/image", verbose_name="تصویر کتاب"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ManyToManyField(
                        null=True,
                        related_name="books_category",
                        to="Library.category",
                        verbose_name="دسته بندی",
                    ),
                ),
                (
                    "leason",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="books_leason",
                        to="Library.leason",
                        verbose_name="درس",
                    ),
                ),
                (
                    "type",
                    models.ManyToManyField(
                        null=True,
                        related_name="books_type",
                        to="Library.category",
                        verbose_name="نوع کتاب",
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        null=True,
                        related_name="books_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربران",
                    ),
                ),
            ],
            options={
                "verbose_name": "کتاب ها",
                "ordering": ("-created",),
            },
        ),
    ]
