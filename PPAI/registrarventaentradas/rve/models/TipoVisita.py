from django.db import models

class TipoVisita(models.Model):

    #Atributos
    
    nombre = models.CharField(max_length=100)
    
    #Metodos 

    #Retorna el nombre del tipoVisita
    def getnombre(self):
        return self.nombre

    #Setea el nombre del tipo de visita
    def setnombre(self,x):
        self.nombre = x
