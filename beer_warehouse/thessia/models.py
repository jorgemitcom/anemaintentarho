from django.db import models
from beer_warehouse.core.models import CommonInfo
from thessia.utils import image_upload_location


# Create your models here.
class Cuento(CommonInfo):
    title = models.CharField('titulo', max_length=50)
    author = models.CharField('autor', max_length=200)
    description = models.CharField('descripcion', max_length=500)
    image = models.ImageField('imagen', blank=True, null=True, upload_to=image_upload_location)
    pages = models.IntegerField('paginas', default=0)
    fpage = models.CharField('ppagina', max_length=10000, default='nada')
    spage =  models.CharField('spagina', max_length=10000, default='nada')
    tpage =  models.CharField('tpagina', max_length=10000, default='nada')

    class Meta():
        verbose_name="Cuento"
        verbose_name_plural="Cuentos"
        ordering=['-title']

    def __str__(self):
        return self.title

class PruebaUno(models.Model):
    concept = models.CharField('concepto', max_length=50)
    definition = models.CharField('definicion', max_length=200)

    class Meta():
        verbose_name="PruebaUno"
        verbose_name_plural="PruebasUno"
        ordering=['-concept']

    def __str__(self):
        return self.definition

class PruebaTres(models.Model):
    def1 = models.CharField('def1', max_length=200)
    def2 = models.CharField('def2', max_length=200)
    def3 = models.CharField('def3', max_length=200)

    class Meta():
        verbose_name="PruebaTres"
        verbose_name_plural="PruebasTres"
        ordering=['pk']

    def __str__(self):
        return "Diferencia 1:" + self.def1 + " // Diferencia 2: " + self.def2 + " // Diferencia 3:" + self.def3