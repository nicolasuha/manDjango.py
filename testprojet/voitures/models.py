from django.db import models

class Automobile(models.Model):
    manufacture = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    date_commercialisation = models.CharField(max_length=100)
    motorisation = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    boite_de_vitesse = models.CharField(max_length=100)

    def __str__(self):
        chaine = f" le modele {model} à été commercialisé en {date_commercialisation} par la marque {manufacture}. Elle possède un moteur {motorisation} en boite de vitesse {boite_de_vitesse} qui délivre sa puissance sur  {transmission}"
        return chaine
