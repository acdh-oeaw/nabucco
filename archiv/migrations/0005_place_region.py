# Generated by Django 3.2.7 on 2022-01-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0004_auto_20220112_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='region',
            field=models.CharField(blank=True, help_text='whatever', max_length=250, verbose_name='Region'),
        ),
    ]