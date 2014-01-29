from django.db import models
from django.utils.translation import ugettext_lazy as _

class Image(models.Model):
    image = models.FileField(upload_to='static/account', verbose_name=_('Image'))
