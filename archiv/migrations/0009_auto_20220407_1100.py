# Generated by Django 3.2.7 on 2022-04-07 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("archiv", "0008_alter_tablet_paraphrase"),
    ]

    operations = [
        migrations.AlterField(
            model_name="archiv",
            name="part_of",
            field=models.ForeignKey(
                blank=True,
                help_text="Place of issue",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rvn_archiv_part_of_place",
                to="archiv.place",
                verbose_name="Provenance",
            ),
        ),
        migrations.AlterField(
            model_name="place",
            name="part_of",
            field=models.ForeignKey(
                blank=True,
                help_text="larger region",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rvn_place_part_of_place",
                to="archiv.place",
                verbose_name="Region",
            ),
        ),
    ]
