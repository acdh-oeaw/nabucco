# Generated by Django 5.1.3 on 2025-01-24 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="newsentry",
            options={
                "ordering": ["updated"],
                "verbose_name": "News Entry",
                "verbose_name_plural": "News Entries",
            },
        ),
    ]