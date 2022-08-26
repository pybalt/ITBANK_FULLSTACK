# Generated by Django 4.0.6 on 2022-08-26 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('direccion_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID Direccion')),
                ('calle', models.CharField(blank=True, max_length=50, null=True, verbose_name='Calle')),
                ('numero', models.IntegerField(blank=True, null=True, verbose_name='Numero')),
                ('ciudad', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ciudad')),
                ('pais', models.CharField(blank=True, max_length=50, null=True, verbose_name='Pais')),
                ('provincia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Provincia')),
            ],
            options={
                'verbose_name': 'direccion',
                'verbose_name_plural': 'direcciones',
                'db_table': 'direcciones',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID Sucursal')),
                ('branch_number', models.IntegerField(verbose_name='Numero de Sucursal')),
                ('branch_name', models.CharField(max_length=50, verbose_name='Nombre de Sucursal')),
                ('branch_address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webitbank.direcciones', verbose_name='Direccion')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'db_table': 'sucursal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Empleado')),
                ('employee_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('employee_surname', models.CharField(max_length=50, verbose_name='Apellido')),
                ('employee_hire_date', models.DateField(verbose_name='Fecha de contratacion')),
                ('employee_dni', models.IntegerField(verbose_name='DNI')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webitbank.sucursal', verbose_name='Sucursal ID')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webitbank.direcciones', verbose_name='Direccion ID')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'managed': True,
            },
        ),
    ]
