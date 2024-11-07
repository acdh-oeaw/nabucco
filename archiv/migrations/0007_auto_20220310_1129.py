# Generated by Django 3.2.7 on 2022-03-10 10:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("archiv", "0006_remove_place_region"),
    ]

    operations = [
        migrations.AddField(
            model_name="archiv",
            name="description",
            field=ckeditor.fields.RichTextField(
                blank=True,
                default="A short description of the archive",
                verbose_name="archive description",
            ),
        ),
        migrations.AddField(
            model_name="archiv",
            name="paragraph",
            field=models.CharField(
                blank=True,
                help_text="siglum according to GMTR 1",
                max_length=25,
                null=True,
                verbose_name="paragraph",
            ),
        ),
        migrations.AddField(
            model_name="place",
            name="description",
            field=ckeditor.fields.RichTextField(
                blank=True,
                default="A very nice place",
                null=True,
                verbose_name="place description",
            ),
        ),
        migrations.AddField(
            model_name="place",
            name="lat",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="place",
            name="lng",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="tablet",
            name="cdli_no",
            field=models.CharField(
                blank=True,
                help_text="Link to CDLI",
                max_length=25,
                verbose_name="CDLI P-Identifier",
            ),
        ),
        migrations.AddField(
            model_name="tablet",
            name="text_number",
            field=models.CharField(
                blank=True,
                help_text="whatever",
                max_length=250,
                verbose_name="Text number",
            ),
        ),
    ]
