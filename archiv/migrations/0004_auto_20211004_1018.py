# Generated by Django 3.2.7 on 2021-10-04 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0003_auto_20210930_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='related_objects',
        ),
        migrations.AddField(
            model_name='place',
            name='related_bib_items',
            field=models.ManyToManyField(blank=True, help_text='whatever', null=True, to='archiv.Bibliography', verbose_name='Bib Item'),
        ),
        migrations.AddField(
            model_name='place',
            name='related_tablets',
            field=models.ManyToManyField(blank=True, help_text='whatever', null=True, to='archiv.Tablet', verbose_name='related tablets'),
        ),
    ]