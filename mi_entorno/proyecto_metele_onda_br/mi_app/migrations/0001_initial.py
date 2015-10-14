# -*- coding: utf-8 -*-
from __future__ import unicode_literals

<<<<<<< HEAD
from django.db import migrations, models
=======
from django.db import models, migrations
>>>>>>> ed5d3204d8f22217a1c2dd27fc3f229841f0d463


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
<<<<<<< HEAD
                ('ciudad', models.ForeignKey(to='mi_app.Ciudad')),
=======
                ('ciudad', models.ForeignKey(related_name='establecimientos', to='mi_app.Ciudad')),
>>>>>>> ed5d3204d8f22217a1c2dd27fc3f229841f0d463
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
<<<<<<< HEAD
                ('fb_id', models.CharField(max_length=200)),
                ('tw_id', models.CharField(max_length=200)),
                ('google_id', models.CharField(max_length=200)),
=======
                ('fb_id', models.CharField(max_length=200, null=True)),
                ('tw_id', models.CharField(max_length=200, null=True)),
                ('google_id', models.CharField(max_length=200, null=True)),
>>>>>>> ed5d3204d8f22217a1c2dd27fc3f229841f0d463
            ],
        ),
        migrations.AddField(
            model_name='establecimiento',
            name='rubro',
<<<<<<< HEAD
            field=models.ForeignKey(to='mi_app.Rubro'),
=======
            field=models.ForeignKey(related_name='establecimientos', to='mi_app.Rubro'),
>>>>>>> ed5d3204d8f22217a1c2dd27fc3f229841f0d463
        ),
        migrations.AddField(
            model_name='ciudad',
            name='provincia',
<<<<<<< HEAD
            field=models.ForeignKey(to='mi_app.Provincia'),
=======
            field=models.ForeignKey(related_name='ciudades', to='mi_app.Provincia'),
>>>>>>> ed5d3204d8f22217a1c2dd27fc3f229841f0d463
        ),
        migrations.AddField(
            model_name='calificacion',
            name='establecimiento',
<<<<<<< HEAD
            field=models.ForeignKey(to='mi_app.Establecimiento'),
=======
            field=models.ForeignKey(related_name='calificaciones', to='mi_app.Establecimiento'),
>>>>>>> ed5d3204d8f22217a1c2dd27fc3f229841f0d463
        ),
        migrations.AddField(
            model_name='calificacion',
            name='usuario',
<<<<<<< HEAD
            field=models.ForeignKey(to='mi_app.Usuario'),
=======
            field=models.ForeignKey(related_name='calificaciones', to='mi_app.Usuario'),
>>>>>>> ed5d3204d8f22217a1c2dd27fc3f229841f0d463
        ),
    ]
