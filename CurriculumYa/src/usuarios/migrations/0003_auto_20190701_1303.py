# Generated by Django 2.1.8 on 2019-07-01 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_perfil_idtipodocu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='IdUsuarios',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='Id usuario'),
        ),
    ]
