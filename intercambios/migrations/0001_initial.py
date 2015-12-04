# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 19:44
from __future__ import unicode_literals
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Intercambio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True)),
                ('status',
                 models.SmallIntegerField(choices=[(1, 'Abierto'), (2, 'Cerrado'), (3, 'Eliminado')], default=1)),
                ('tipo', models.SmallIntegerField(choices=[(1, 'Público'), (2, 'Privado')], default=2)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_intercambio', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_invitado', models.EmailField(max_length=254)),
                ('mensaje', models.TextField(blank=True)),
                ('intercambio',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intercambios.Intercambio')),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_admin', models.BooleanField(default=False)),
                ('amigo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                            related_name='amigo', to=settings.AUTH_USER_MODEL)),
                ('intercambio',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intercambios.Intercambio')),
                (
                'usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='intercambio',
            name='amigos',
            field=models.ManyToManyField(through='intercambios.Participante', to=settings.AUTH_USER_MODEL),
        ),
    ]
