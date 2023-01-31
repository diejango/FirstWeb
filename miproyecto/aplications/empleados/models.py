from django.db import models
from aplications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class abilitie (models.Model):
    """Model definition fos Habilitie ."""
    abilitie = models.CharField('abilitie', max_length=50)
    # TODO: Define fields here

    class Meta:
        """Meta definition fos Habilitie ."""

        verbose_name ='abilitie'
        verbose_name_plural ='abilities'

    def __str__(self):
        return str(self.id) + '-' + self.abilitie


class Empleado (models.Model):
    jobchoices=(
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','PROGRAMADOR'),
        ('3','ECONOMISTA'),
        ('4','OTRO')
    )
    first_name = models.CharField('nombres', max_length=50)
    last_name = models.CharField('apellidos', max_length=50)
    full_name = models.CharField('nombre completo', max_length=100,blank=True)
    job = models.CharField('trabajo', max_length=1,choices=jobchoices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='empleado', blank=True,null=True)
    abilities = models.ManyToManyField(abilitie)
    hoja_vida = RichTextField(blank=True)
    
    class Meta:
          verbose_name='employee'
          verbose_name_plural='employees'
          unique_together=('first_name','last_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name