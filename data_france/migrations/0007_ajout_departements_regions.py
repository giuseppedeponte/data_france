# Generated by Django 3.0.5 on 2020-04-07 07:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("data_france", "0006_search"),
    ]

    operations = [
        migrations.RemoveField(model_name="commune", name="code_departement",),
        migrations.AddField(
            model_name="epci",
            name="geometry",
            field=django.contrib.gis.db.models.fields.MultiPolygonField(
                editable=False,
                geography=True,
                null=True,
                srid=4326,
                verbose_name="Géométrie",
            ),
        ),
        migrations.AddField(
            model_name="epci",
            name="population",
            field=models.PositiveIntegerField(null=True, verbose_name="Population"),
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        editable=False, max_length=3, unique=True, verbose_name="Code"
                    ),
                ),
                (
                    "nom",
                    models.CharField(
                        editable=False, max_length=200, verbose_name="Nom de la région"
                    ),
                ),
                (
                    "type_nom",
                    models.PositiveSmallIntegerField(
                        editable=False, verbose_name="Type de nom"
                    ),
                ),
                (
                    "population",
                    models.PositiveIntegerField(null=True, verbose_name="Population"),
                ),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.MultiPolygonField(
                        editable=False,
                        geography=True,
                        null=True,
                        srid=4326,
                        verbose_name="Géométrie",
                    ),
                ),
                (
                    "chef_lieu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        related_query_name="chef_lieu_de",
                        to="data_france.Commune",
                    ),
                ),
            ],
            options={"ordering": ("nom",), "verbose_name": "Région"},
        ),
        migrations.CreateModel(
            name="Departement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        editable=False, max_length=3, unique=True, verbose_name="Code"
                    ),
                ),
                (
                    "nom",
                    models.CharField(
                        editable=False,
                        max_length=200,
                        verbose_name="Nom du département",
                    ),
                ),
                (
                    "type_nom",
                    models.PositiveSmallIntegerField(
                        editable=False, verbose_name="Type de nom du département"
                    ),
                ),
                (
                    "population",
                    models.PositiveIntegerField(null=True, verbose_name="Population"),
                ),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.MultiPolygonField(
                        editable=False,
                        geography=True,
                        null=True,
                        srid=4326,
                        verbose_name="Géométrie",
                    ),
                ),
                (
                    "chef_lieu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        related_query_name="chef_lieu_de",
                        to="data_france.Commune",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="departements",
                        related_query_name="departement",
                        to="data_france.Region",
                    ),
                ),
            ],
            options={"ordering": ("code",), "verbose_name": "Département"},
        ),
        migrations.AddField(
            model_name="commune",
            name="departement",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="communes",
                related_query_name="commune",
                to="data_france.Departement",
            ),
        ),
    ]
