# Generated by Django 2.2.1 on 2019-05-12 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosUsua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdDatosUsua', models.IntegerField()),
                ('IdUsuarios', models.IntegerField()),
                ('IdTipoUsua', models.IntegerField()),
                ('IdTipoDocu', models.IntegerField()),
                ('IdEstaCivil', models.IntegerField()),
                ('IdEtnias', models.IntegerField()),
                ('IdCiudades', models.IntegerField()),
                ('IdDepartamentos', models.IntegerField()),
                ('IdPaises', models.IntegerField()),
                ('PerfilPro', models.TextField()),
                ('Genero', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdUsuarios', models.IntegerField()),
                ('IdTipoUsua', models.IntegerField()),
                ('NombUsua', models.CharField(max_length=50)),
                ('ApellUsua', models.CharField(max_length=50)),
                ('EmailUsua', models.CharField(max_length=50)),
                ('EstaUsua', models.CharField(max_length=50)),
            ],
        ),
    ]
