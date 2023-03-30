from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=50)
    descrição = models.TextField()
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    altura = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.ImageField(upload_to = 'img', blank = True, null = True)

    def __str__(self):
        return self.nome

class Especie(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
