# Generated by Django 4.0.6 on 2022-08-22 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('card_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Tarjeta')),
                ('numero_tarjeta', models.IntegerField(verbose_name='Numero de Tarjeta')),
                ('cvv', models.IntegerField(verbose_name='CVV')),
                ('fecha_otorgamiento', models.DateField(auto_now_add=True, verbose_name='Fecha de otorgamiento')),
                ('fecha_expiracion', models.DateField(verbose_name='Fecha de expiracion')),
                ('marca_tarjeta', models.CharField(choices=[('VS', 'VISA'), ('MC', 'MASTERCARD'), ('AE', 'AMERICAN EXPRESS')], max_length=25, verbose_name='Tarjeta')),
                ('account_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuentas.cuenta', verbose_name='ID Cuenta')),
            ],
            options={
                'verbose_name': 'Tarjeta',
                'verbose_name_plural': 'Tarjetas',
                'db_table': 'cards',
                'managed': True,
            },
        ),
    ]
