# Generated by Django 3.1.7 on 2021-08-17 09:41

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_france', '0029_deputes_europeens'),
    ]

    operations = [
        migrations.AddField(
            model_name='depute',
            name='search',
            field=django.contrib.postgres.search.SearchVectorField(null=True, verbose_name='Champ de recherche'),
        ),
        migrations.AddField(
            model_name='deputeeuropeen',
            name='search',
            field=django.contrib.postgres.search.SearchVectorField(null=True, verbose_name='Champ de recherche'),
        ),
        migrations.AddField(
            model_name='eludepartemental',
            name='search',
            field=django.contrib.postgres.search.SearchVectorField(null=True, verbose_name='Champ de recherche'),
        ),
        migrations.AddField(
            model_name='eluregional',
            name='search',
            field=django.contrib.postgres.search.SearchVectorField(null=True, verbose_name='Champ de recherche'),
        ),
    ]