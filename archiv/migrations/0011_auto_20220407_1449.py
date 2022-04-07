# Generated by Django 3.2.7 on 2022-04-07 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0010_auto_20220407_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archiv',
            name='legacy_pk',
            field=models.IntegerField(blank=True, help_text='NaBuCCo No.', null=True, verbose_name='Archive ID'),
        ),
        migrations.AlterField(
            model_name='archiv',
            name='name',
            field=models.CharField(blank=True, help_text='Following GMTR 1', max_length=250, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='archiv',
            name='part_of',
            field=models.ForeignKey(blank=True, help_text='(Assumed) place of origin', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_archiv_part_of_place', to='archiv.place', verbose_name='Provenance'),
        ),
    ]