from django.db import models

class Automobile(models.Model):
    manufacture = models.TextField(null = True, blank = True)
    model = models.TextField(null = True, blank = True)
    date_commercialisation = models.TextField(null = True, blank = True)
    motorisation = models.TextField(null = True, blank = True)
    transmission = models.TextField(null = True, blank = True)
    boite_de_vitesse = models.TextField(null = True, blank = True)
    type = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f" le modele {self.model} à été commercialisé en {self.date_commercialisation} par la marque {self.manufacture}. Elle possède un moteur {self.motorisation} en boite de vitesse {self.boite_de_vitesse} qui délivre sa puissance sur  {self.transmission}"
        return chaine

class Marque(models.Model):
    Marque = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f" veuillez indiquer le nom de la marque dont vous souhaitez voir les voitures : {self.Marque}"
        return chaine