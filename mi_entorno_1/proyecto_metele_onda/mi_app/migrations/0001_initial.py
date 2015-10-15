# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('puntaje', models.IntegerField()),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('codigo_postal', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('ciudad', models.ForeignKey(related_name='establecimientos', to='mi_app.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fb_id', models.CharField(max_length=200, null=True)),
                ('tw_id', models.CharField(max_length=200, null=True)),
                ('google_id', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='establecimiento',
            name='rubro',
            field=models.ForeignKey(related_name='establecimientos', to='mi_app.Rubro'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='provincia',
            field=models.ForeignKey(related_name='ciudades', to='mi_app.Provincia'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='establecimiento',
            field=models.ForeignKey(related_name='calificaciones', to='mi_app.Establecimiento'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='usuario',
            field=models.ForeignKey(related_name='calificaciones', to='mi_app.Usuario'),
        ),
    ]
