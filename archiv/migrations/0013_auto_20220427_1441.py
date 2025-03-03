# Generated by Django 3.2.7 on 2022-04-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archiv", "0012_alter_place_legacy_pk"),
    ]

    operations = [
        migrations.AlterField(
            model_name="glossary",
            name="legacy_pk",
            field=models.IntegerField(
                blank=True, help_text="whatever", null=True, verbose_name="Concept ID"
            ),
        ),
        migrations.AlterField(
            model_name="tablet",
            name="legacy_pk",
            field=models.IntegerField(
                blank=True, help_text="whatever", null=True, verbose_name="NaBuCCo No."
            ),
        ),
    ]
