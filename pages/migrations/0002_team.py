# Generated by Django 4.2.6 on 2023-11-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=40)),
                ("title", models.CharField(max_length=40)),
                ("image", models.ImageField(upload_to="teams/")),
                (
                    "facebook_url",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "twitter_url",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "linkedin_url",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
            options={
                "verbose_name_plural": "teams",
                "ordering": ["-id"],
            },
        ),
    ]
