# Generated by Django 4.0.6 on 2022-08-25 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID Cuenta')),
                ('balance', models.IntegerField(verbose_name='Balance')),
                ('tipo_cuenta', models.CharField(choices=[('CAP', 'CAJA DE AHORRO EN PESOS'), ('CAD', 'CAJA DE AHORRO EN DOLARES'), ('CC', 'CUENTA CORRIENTE')], max_length=10, verbose_name='Tipo de cuenta')),
                ('iban', models.CharField(editable=False, max_length=10, verbose_name='IBAN. \n                            Dejar en Blanco para generar automaticamente')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente', verbose_name='Cliente')),
            ],
            options={
                'db_table': 'cuenta',
                'managed': True,
            },
        ),
    ]
