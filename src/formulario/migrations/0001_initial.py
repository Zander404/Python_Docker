# Generated by Django 3.1.2 on 2022-06-07 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('numero', models.DecimalField(decimal_places=0, max_digits=6)),
            ],
            options={
                'db_table': 'banco',
            },
        ),
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=200)),
                ('fone', models.DecimalField(decimal_places=0, max_digits=11, unique=True)),
                ('tipo', models.DecimalField(decimal_places=0, max_digits=2)),
                ('fone1', models.DecimalField(decimal_places=0, max_digits=11, unique=True)),
                ('tipo1', models.DecimalField(decimal_places=0, max_digits=2)),
                ('agencia', models.CharField(max_length=100)),
                ('nome_Agencia', models.CharField(max_length=100)),
                ('id_banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulario.banco')),
            ],
            options={
                'db_table': 'agencia',
            },
        ),
    ]
