# Generated by Django 3.2.7 on 2021-09-21 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archiv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('legacy_pk', models.IntegerField(blank=True, help_text='whatever', null=True, verbose_name='alt id')),
                ('name', models.CharField(blank=True, help_text='whatever', max_length=250, verbose_name='name')),
                ('alt_name', models.CharField(blank=True, help_text='whatever', max_length=250, verbose_name='Alternative name')),
                ('title', models.CharField(blank=True, help_text='whatever', max_length=250, verbose_name='Title')),
                ('related_objects', models.IntegerField(blank=True, help_text='TODO', null=True, verbose_name='related objects')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
                ('part_of', models.ForeignKey(blank=True, help_text='whatever', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_archiv_part_of_archiv', to='archiv.archiv', verbose_name='part of')),
            ],
            options={
                'verbose_name': 'Archiv',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Bibliography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('legacy_pk', models.IntegerField(blank=True, help_text='whatever', null=True, verbose_name='alt id')),
                ('short_title', models.CharField(blank=True, help_text='whatever', max_length=250, verbose_name='Short Title')),
                ('author', models.CharField(blank=True, help_text='whatever', max_length=250, verbose_name='Author')),
                ('publication_year', models.CharField(blank=True, help_text='whatever', max_length=250, verbose_name='Publication year')),
                ('title', models.CharField(blank=True, help_text='whatever', max_length=250, verbose_name='Title')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
            ],
            options={
                'verbose_name': 'Bibliography',
                'ordering': ['short_title'],
            },
        ),
        migrations.CreateModel(
            name='Glossary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('legacy_pk', models.IntegerField(blank=True, help_text='whatever', null=True, verbose_name='alt id')),
                ('pref_label', models.CharField(blank=True, help_text='whatever', max_length=250, verbose_name='pref label')),
                ('hierarchy', models.CharField(blank=True, help_text='whatever', max_length=250, verbose_name='Hierarchy')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
            ],
            options={
                'verbose_name': 'Glossary',
                'ordering': ['pref_label'],
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('legacy_pk', models.IntegerField(blank=True, help_text='whatever', null=True, verbose_name='alt id')),
                ('name', models.CharField(blank=True, help_text='whatever', max_length=250, verbose_name='Name')),
                ('related_objects', models.IntegerField(blank=True, help_text='TODO', null=True, verbose_name='related objects')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
                ('part_of', models.ForeignKey(blank=True, help_text='whatever', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_place_part_of_place', to='archiv.place', verbose_name='part of')),
            ],
            options={
                'verbose_name': 'Place',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('legacy_pk', models.IntegerField(blank=True, help_text='whatever', null=True, verbose_name='alt id')),
                ('museum_id', models.CharField(blank=True, help_text='whatever', max_length=250, verbose_name='Museum No.')),
                ('paraphrase', models.TextField(blank=True, help_text='whatever', null=True, verbose_name='Paraphrase')),
                ('transliteration', models.TextField(blank=True, help_text='whatever', null=True, verbose_name='Transliteration')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
                ('archiv', models.ForeignKey(blank=True, help_text='whatever', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_tablet_archiv_archiv', to='archiv.archiv', verbose_name='Archive')),
                ('place_of_issue', models.ForeignKey(blank=True, help_text='whatever', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_tablet_place_of_issue_place', to='archiv.place', verbose_name='Place of issue')),
                ('type_content', models.ForeignKey(blank=True, help_text='whatever', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_tablet_type_content_glossary', to='archiv.glossary', verbose_name='Type and content')),
            ],
            options={
                'verbose_name': 'Tablet',
                'ordering': ['id'],
            },
        ),
    ]
