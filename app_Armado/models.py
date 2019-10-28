from django.db import models

# Create your models here.

from django.utils.translation import ugettext as _
class Meta:
        permissions = (
            ('Tecnico',_('Es Tecnico')),
            ('Cliente',_('Es Cliente')),
        )
