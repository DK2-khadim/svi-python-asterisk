from django.db import models

# Create your models here.


class Client(models.Model):
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    numero = models.IntegerField()
    codeSecret = models.IntegerField()
    solde = models.IntegerField(default=0)

    def __str__(self):
        return f"Compte de {self.prenom} {self.nom}"


