from django.db import models

# Create your models here.


class Banco(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False,

    )

    numero = models.DecimalField(
        max_digits=6,
        decimal_places=0,
        null=False,
        blank=False,
    )


    class Meta:
        db_table = "banco"
    



class Agencia(models.Model):
    
    endereco = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    
    fone = models.DecimalField(
        max_digits=11,
        decimal_places=0,
        blank=False,
        null=False,
        unique=True,
    )

    tipo = models.DecimalField(
        decimal_places=0,
        max_digits=2,        
    )

    fone1 = models.DecimalField(
        max_digits=11,
        decimal_places=0,
        blank=False,
        null=False,
        unique=True,
    )

    tipo1 = models.DecimalField(
        decimal_places=0,
        max_digits=2,
    )

    agencia = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    nome_Agencia = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    
    id_banco = models.ForeignKey(
        'banco',
        on_delete=models.CASCADE,
    )

    
    class Meta:
        db_table = "agencia"

