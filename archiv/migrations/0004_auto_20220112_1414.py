# Generated by Django 3.2.7 on 2022-01-12 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0003_auto_20211112_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['name'], 'verbose_name': 'Place'},
        ),
        migrations.RemoveField(
            model_name='place',
            name='broader_concept',
        ),
        migrations.RemoveField(
            model_name='place',
            name='level',
        ),
        migrations.RemoveField(
            model_name='place',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='place',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='place',
            name='tree_id',
        ),
    ]
