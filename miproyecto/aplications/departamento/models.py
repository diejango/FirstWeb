from django.db import models

# Create your models here.

class Departamento(models.Model):
     name = models.CharField('nombre', max_length=50,null =  True)
     shorname = models.CharField('Nombre Corto', max_length=20,blank=True,unique=True)
     anulate = models.BooleanField('anulado',default=False)

     class Meta:
          verbose_name='apartment'
          verbose_name_plural='apartments'
          unique_together=('name','shorname')


     def __str__(self) :
          return str(self.id) + '-' + self.name 