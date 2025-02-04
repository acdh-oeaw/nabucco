# Generated by Django 5.1.3 on 2025-02-04 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archiv", "0028_tablet_regional_setting"),
    ]

    operations = [
        migrations.CreateModel(
            name="VanDrielFiles",
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
                    "file",
                    models.CharField(
                        choices=[
                            (
                                "01",
                                "1. Administrative Management and Jurisdiction - General",
                            ),
                            (
                                "02",
                                "2. Administrative Jurisdiction and Accounting - Animals",
                            ),
                            (
                                "03",
                                "3. Administrative Jurisdiction and Accounting - Personnel",
                            ),
                            ("04", "4. Accounting - Silver"),
                            ("05", "5. Personnel and food rations"),
                            ("06", "6. Prebends"),
                            ("07", "7. Crafts"),
                            ("08", "8. Real estate"),
                            ("09", "9. Agricultural products"),
                            ("10", "10. Animal husbandry"),
                            ("11", "11. Letters"),
                            ("12", "12. Unclassified"),
                        ],
                        default="12",
                        help_text="overarching file category",
                        max_length=2,
                        verbose_name="File",
                    ),
                ),
                (
                    "sub_file",
                    models.CharField(
                        default="z. not defined",
                        help_text="Text type or topic",
                        max_length=250,
                        verbose_name="Sub-file",
                    ),
                ),
                (
                    "verbum_regens",
                    models.CharField(
                        blank=True,
                        help_text="Akkadian key term for text identification",
                        max_length=250,
                        null=True,
                        verbose_name="Verbum regens",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="General description and remarks concerning a file",
                        null=True,
                        verbose_name="Description",
                    ),
                ),
            ],
            options={
                "verbose_name": "File after van Driel, BiOr 55-1 (1998), 59-79",
                "verbose_name_plural": "Files after van Driel, BiOr 55-1 (1998), 59-79",
                "ordering": ["file", "sub_file"],
            },
        ),
    ]
