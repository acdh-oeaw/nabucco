# Generated by Django 5.1.3 on 2024-11-20 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archiv", "0020_alter_archiv_alt_name_alter_bibliography_author_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tablet",
            name="inferred_date",
            field=models.CharField(
                blank=True,
                help_text="date range on basis of context and prosopography",
                max_length=250,
                verbose_name="Inferred date",
            ),
        ),
    ]
