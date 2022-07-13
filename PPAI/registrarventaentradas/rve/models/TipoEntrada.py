from django.db import models

class TipoEntrada(models.Model):

    #Atributos
    
    nombre = models.CharField(max_length=100)
    
    #Metodos 

    #Retorna el nombre del tipo de entrada
    def getnombre(self):
        return self.nombre

    #Setea el nombre del tipo de entrada
    def setnombre(self,x):
        self.nombre = x
