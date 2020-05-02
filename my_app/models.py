from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    # esto hace que en vez de  devolver un item devuelve el str con el que fue almacenado
    def __str__(self):
        return '{}'.format(self.search) 

    # esto agrega el estilo plural a la palabra que tu quieras
    class Meta:
        verbose_name_plural = 'Searches'
