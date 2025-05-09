# Generated by Django 5.1.3 on 2025-01-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archiv", "0023_alter_archiv_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkPackage",
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
                    "wp_number",
                    models.CharField(
                        blank=True,
                        help_text="Number of the work package",
                        max_length=250,
                        null=True,
                        verbose_name="Number of the work package",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="Title of the work package",
                        max_length=250,
                        null=True,
                        verbose_name="Title of the work package",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Description of the work package",
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                (
                    "wp_lead",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Jena", "Jena team"),
                            ("Vienna", "Vienna team"),
                            ("Warsaw", "Warsaw team"),
                            ("ext", "diverse team"),
                        ],
                        help_text="Lead of the work package",
                        max_length=250,
                        null=True,
                        verbose_name="Work package lead",
                    ),
                ),
            ],
            options={
                "verbose_name": "Work Package",
                "verbose_name_plural": "Work Packages",
                "ordering": ["wp_number"],
            },
        ),
    ]
