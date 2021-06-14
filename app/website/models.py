from django.db import models

# Create your models here.
class Empleado(models.Model):
    sex_choices = (
        ('H','Hombre'),
        ('M','Mujer'),
        ('O','Otro'),
    )
    name = models.CharField(max_length=50)
    l_names = models.CharField(max_length=100)
    superior_id = models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True)
    sex = models.CharField(max_length=1,choices=sex_choices)
    b_date = models.DateField()

    def __str__(self):
        return self.name + " " + self.l_names

class Cliente(models.Model):
    sex_choices = (
        ('H','Hombre'),
        ('M','Mujer'),
        ('O','Otro'),
    )
    name = models.CharField(max_length=50)
    l_names = models.CharField(max_length=100)
    works_with = models.ForeignKey("Empleado",on_delete=models.SET_NULL,null=True)
    sex = models.CharField(max_length=1,choices=sex_choices)
    b_date = models.DateField(null=True)
    ct_id = models.ForeignKey("C_tarjeta",on_delete=models.SET_NULL,null=True,blank=True)
    dt_id = models.ForeignKey("D_tarjeta",on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name + " " + self.l_names

class C_tarjeta(models.Model):
    num_tarjeta = models.CharField(max_length=16,null=True,blank=True)
    credito = models.FloatField()
    c_disponible = models.FloatField(null=True,blank=True)
    saldo = models.FloatField(default=0,null=True,blank=True)
    dia_corte = models.IntegerField(null=True,blank=True)
    fecha_valida = models.DateField(null=True,blank=True)
    cliente_id = models.ForeignKey("Cliente",on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        number = str(self.num_tarjeta)
        return number[0:4] + '-' + number[4:8] + '-' + number[8:12] + '-' + number[12:]

class D_tarjeta(models.Model):
    num_tarjeta = models.CharField(max_length=16,null=True,blank=True)
    balance = models.FloatField()
    fecha_valida = models.DateField(null=True,blank=True)
    cliente_id = models.ForeignKey("Cliente",on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        number = str(self.num_tarjeta)
        return number[0:4] + '-' + number[4:8] + '-' + number[8:12] + '-' + number[12:]