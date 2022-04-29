from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AutomobileForm(ModelForm):
    class Meta:
        model = models.Automobile
        fields = ('manufacture', 'model', 'date_commercialisation', 'motorisation','transmission','boite_de_vitesse')
        labels = {
            'manufacture' : _('manufacture'),
            'model' : _('model') ,
            'date_commercialisation' : _('date_commercialisation'),
            'motorisation' : _('motorisation'),
            'transmission' : _('transmission')
            'boite_de_vitesse': _('boite_de_vitesse')
            }
