from django.db import models

class Animal(models.Model):
    nombre_vulgar = models.CharField(max_length=100)
    nombre_cientifico = models.CharField(max_length=150, unique=True)
    familia = models.CharField(max_length=100)
    en_peligro = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_vulgar

class Zoo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    tamano_m2 = models.IntegerField()
    presupuesto_anual = models.DecimalField(max_digits=12, decimal_places=2)
    animales = models.ManyToManyField(Animal, related_name="zoos")

    def __str__(self):
        return self.nombre