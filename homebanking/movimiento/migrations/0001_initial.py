# Generated by Django 4.0.6 on 2022-08-25 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('movimiento_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Movimiento')),
                ('monto', models.IntegerField(verbose_name='Monto')),
                ('tipo_movimiento', models.CharField(choices=[('TRF', 'TRANSFERENCIA'), ('RTC', 'RETIRO EN CAJERO'), ('PR', 'PRESTAMO')], max_length=10, verbose_name='Tipo de Movimiento')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('cuenta_destinatario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuenta_destinatario_id', to='cuentas.cuenta', verbose_name='Destinatario')),
                ('cuenta_remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuenta_remitente_id', to='cuentas.cuenta', verbose_name='Remitente')),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
                'db_table': 'movimientos',
                'managed': True,
            },
        ),
    ]
