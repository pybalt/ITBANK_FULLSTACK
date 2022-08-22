from django.db import models
from clientes.models import Cliente
# Create your models here.
"""21/08/22"""


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    customer_id = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE, to_field="customer_id")

    class Meta:
        managed = True
        db_table = 'prestamo'
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'