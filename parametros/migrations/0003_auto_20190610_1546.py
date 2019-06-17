# Generated by Django 2.2.1 on 2019-06-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0002_auto_20190610_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombTiCa', models.CharField(default='', max_length=255, verbose_name='Nombre tipo de cargo')),
            ],
            options={
                'verbose_name': 'Tipo de cargo',
                'verbose_name_plural': 'Tipos de cargos',
            },
        ),
        migrations.DeleteModel(
            name='Cargo',
        ),
    ]
