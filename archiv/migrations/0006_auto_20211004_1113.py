# Generated by Django 3.2.7 on 2021-10-04 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0005_auto_20211004_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archiv',
            name='related_objects',
        ),
        migrations.RemoveField(
            model_name='glossary',
            name='related_objects',
        ),
        migrations.AddField(
            model_name='archiv',
            name='related_bib_items',
            field=models.ManyToManyField(blank=True, help_text='whatever', to='archiv.Bibliography', verbose_name='Bib Item'),
        ),
        migrations.AddField(
            model_name='archiv',
            name='related_tablets',
            field=models.ManyToManyField(blank=True, help_text='whatever', related_name='rvn_archiv_tablets', to='archiv.Tablet', verbose_name='related tablets'),
        ),
        migrations.AddField(
            model_name='bibliography',
            name='related_bib_items',
            field=models.ManyToManyField(blank=True, help_text='whatever', to='archiv.Bibliography', verbose_name='Bib Item'),
        ),
        migrations.AddField(
            model_name='bibliography',
            name='related_tablets',
            field=models.ManyToManyField(blank=True, help_text='whatever', related_name='rvn_bibliography_tablets', to='archiv.Tablet', verbose_name='related tablets'),
        ),
        migrations.AddField(
            model_name='glossary',
            name='related_bib_items',
            field=models.ManyToManyField(blank=True, help_text='whatever', to='archiv.Bibliography', verbose_name='Bib Item'),
        ),
        migrations.AddField(
            model_name='glossary',
            name='related_tablets',
            field=models.ManyToManyField(blank=True, help_text='whatever', to='archiv.Tablet', verbose_name='related tablets'),
        ),
        migrations.AlterField(
            model_name='bibliography',
            name='related_objects',
            field=models.CharField(blank=True, help_text='tablets published', max_length=250, verbose_name='related objects'),
        ),
    ]