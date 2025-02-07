# Generated by Django 5.1.3 on 2025-02-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archiv", "0030_tablet_van_driel_files"),
    ]

    operations = [
        migrations.AddField(
            model_name="tablet",
            name="private_context",
            field=models.BooleanField(
                default=False,
                help_text="Does the text pertain to a private (economic) context?",
                verbose_name="Private context",
            ),
        ),
    ]
